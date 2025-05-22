import streamlit as st
import joblib
import numpy as np
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import regex as re
from contractions import fix
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from sklearn.mixture import GaussianMixture
from sklearn.preprocessing import MinMaxScaler

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

embedding_model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')

def prep_text(text):
    text = fix(text)
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", '', text)
    text = re.sub(r"\s+", ' ', text).strip()
    text = tokenize_and_remove_stopwords(text)
    return embedding_model.encode(text)

def tokenize_and_remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text)
    return " ".join([word for word in tokens if word not in stop_words])

all_true_data = pd.read_csv("test_data/True.csv")["text"].tolist()
trusted_embeddings = [prep_text(text) for text in all_true_data]

gmm = GaussianMixture(n_components=1, covariance_type='full', random_state=42)
gmm.fit(trusted_embeddings)
joblib.dump(gmm, "gmm_model.joblib")
