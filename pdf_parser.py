import os
import fitz
import regex as re
import csv

folder_path = "pdf_data"

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    text = re.sub(r"\s+", ' ', text).strip()
    return text
def saveData(article,url,article_title):
    file_exists = os.path.isfile('article_output.csv')
    data = [
                {"title": article_title, "content": article, "link": url}
            ]
    with open('article_output.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["title", "content", "link"])
        if not file_exists:
            writer.writeheader()
        writer.writerows(data)
        print(f"{article_title} has been Successfully Recorded!")
def standardize_fileNames(filename):
    return re.sub(r'[^\w\s-]', '', filename).strip()

pdf_files = [(os.path.join(folder_path, f),f) for f in os.listdir(folder_path) if f.lower().endswith('.pdf')]
pdf_texts = [(extract_text_from_pdf(filePath),standardize_fileNames(fileName)[:-3]+".pdf",standardize_fileNames(fileName[:-4])) for filePath,fileName in pdf_files]
for article,article_title,url in pdf_texts:
    saveData(article,article_title,url)