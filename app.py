import pandas as pd
from langdetect import detect
from collections import Counter
import re
import unicodedata
from contractions import fix
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sentence_transformers import SentenceTransformer
from sklearn.mixture import GaussianMixture
import numpy as np
from scipy.spatial.distance import mahalanobis
import spacy
import streamlit as st
import joblib
from sklearn.decomposition import PCA
import plotly.express as px

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

st.title("DUDAINFO PH")

article_outcome= pd.read_csv("article_outcomes_final.csv")
model = joblib.load('gmm_anomaly_general_detector.joblib')

contractions_filipino_ver = {
    "sakin": "sa akin",
    "sayo": "sa iyo",
    "sakanya": "sa kanya",
    "satin": "sa atin",
    "samin": "sa amin",
    "sainyo": "sa inyo",
    "sakanila": "sa kanila",
    "sa'to": "sa ito",
    "sa'yan": "sa iyan",
    "sa'yon": "sa iyon",
    "dito": "sa ito",
    "diyan": "sa iyan",
    "doon": "sa iyon",
    "ngakin": "ng akin",
    "ngiyo": "ng iyo",
    "ngkanya": "ng kanya",
    "ngamin": "ng amin",
    "ngatin": "ng atin",
    "nginyo": "ng inyo",
    "ngkanila": "ng kanila",
    "di'ko": "hindi ako",
    "di'mo": "hindi mo",
    "di'ya": "hindi siya",
    "di'la": "hindi nila",
    "wala'ko": "wala ako",
    "nasa'kin": "nasa akin",
    "ako'y": "ako ay",
    "ika'y": "ikaw ay",
    "siya'y": "siya ay",
    "tayo'y": "tayo ay",
    "kami'y": "kami ay",
    "sila'y": "sila ay"
}

def unicode_data(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8')
    return text
def handle_tokens(text,lang):
    match lang:
        case "en":
            stop_words = set(stopwords.words('english'))
            tokens = word_tokenize(text)
            text = " ".join([word for word in tokens if word not in stop_words])
        case "tl":
            nlp = spacy.load("tl_core_news_sm")
            doc = nlp(text)
            text = " ".join([token.text for token in doc if not token.is_stop])
    return text
def handle_contractions(text,lang):
    match lang:
        case "en":
            text = fix(text)
        case "tl":
            for contraction, expansion in contractions_filipino_ver.items():
                text = text.replace(contraction, expansion)
    return text
def general_text_preparation(text, lang=None):
    if not isinstance(text, str):
        if pd.isna(text):
            return ""
        text = str(text)
    text = unicode_data(text)
    text = text.lower()
    if lang:
        text = handle_contractions(text, lang)
    if lang:
        text = handle_tokens(text, lang)
    text = re.sub(r"[^a-zA-Z0-9\sáéíóúñü]", '', text)
    text = re.sub(r"\s+", ' ', text).strip()
    return text

article_title = st.text_input("Enter your article title here:")
article_content = st.text_area("Enter your article content here:")
article_link = st.text_input("Enter your article Link here:")

if article_title and article_content and article_link:

    mini_df = {
        "title":[article_title],
        "content":[article_content],
        "link":[article_link]
    }
    mini_df = pd.DataFrame(mini_df)

    mini_df["content"] = mini_df.apply(
        lambda row: general_text_preparation(
            text=row["content"],
            lang=row.name
        ),
        axis=1
    )
    text = mini_df["content"].fillna("").astype(str).tolist()
    embedder = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
    embeddings = embedder.encode(text,normalize_embeddings=True)

    log_likelihoods = model.score_samples(embeddings)  
    mini_df["anomaly_score"] = -log_likelihoods

    training_anomaly_scores = np.load('training_anomaly_scores.npy')
    threshold = np.quantile(training_anomaly_scores, 0.95)

    new_article_score = mini_df.loc[0, "anomaly_score"]

    st.write(f"### Anomaly Score (How weird is this article?): {new_article_score:.4f}")
    st.write(f"Current anomaly detection threshold: {threshold:.4f}")

    if new_article_score > threshold:
        st.error("⚠️ This article is considered anomalous (unusual) compared to your data.")
    else:
        st.success("✅ This article appears normal based on the current model.")

    mini_df["is_anomaly"] = (mini_df["anomaly_score"] > threshold).astype(int)

    anomalies = mini_df.sort_values("anomaly_score", ascending=False)
    st.write(anomalies[["content", "anomaly_score", "is_anomaly"]])

    labels = model.predict(embeddings)

    anomalies = mini_df["is_anomaly"].astype(bool).values

    new_data_pred = model.predict([embeddings[0]])[0]
    same_label_indices = np.where(model.predict(embeddings) == new_data_pred)[0]
    component_points = embeddings[same_label_indices]

    mean = model.means_[new_data_pred]
    cov = model.covariances_[new_data_pred]

    try:
        inv_cov = np.linalg.inv(cov)
    except np.linalg.LinAlgError:
        cov += np.eye(cov.shape[0]) * 1e-6
        inv_cov = np.linalg.inv(cov)

    distances = [mahalanobis(x, mean, inv_cov) for x in component_points]
    sorted_local_indices = np.argsort(distances)
    nearest_articles_ind = same_label_indices[sorted_local_indices[:5]]

    row_ind = []
    for i, idx in enumerate(nearest_articles_ind):
        row_ind.append(idx)

    deemed_references = article_outcome.iloc[row_ind]
    st.write(deemed_references)

    closest_dist = distances[sorted_local_indices[0]]
    if closest_dist < 1.5:
        st.success("🟢 This article is closely aligned with existing references.")
    elif closest_dist < 3.0:
        st.warning("🟡 This article is somewhat referenced, but distant.")
    else:
        st.error("🔴 This article is significantly different from typical references.")