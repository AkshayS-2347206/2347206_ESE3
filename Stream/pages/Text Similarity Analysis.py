import pandas as pd
import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import re

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df = pd.read_csv("ecommerce_dataset.csv")
df = df.dropna(subset=["Review Text"])
df = df[df["Review Text"].astype(str).str.strip() != ""]

def preprocess_text(text):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words and token not in string.punctuation]

    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]
    
    filtered_tokens = [re.sub(r'[^a-zA-Z0-9\s]', '', token) for token in lemmatized_tokens]
    filtered_tokens = [token.lower() for token in filtered_tokens]
    preprocessed_text = ' '.join(filtered_tokens)
    
    return preprocessed_text

df['Cleaned Review Text'] = df['Review Text'].apply(preprocess_text)

st.title("Preprocessed Review Text")
st.write(df[['Review Text', 'Cleaned Review Text']])
