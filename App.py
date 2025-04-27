import numpy as np
import pandas as pd
import streamlit as st
import requests
import pickle
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
nltk.download('stopwords')

ps=PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = text.split()  # Split into words
    y = [word for word in text if word.isalnum()]  # Keep only alphanumeric words

    text=y[:]
    y.clear()

    for word in text:
        if word not in stopwords.words('english') and word not in string.punctuation:
            y.append(word)
    

    text=y[:]
    y.clear()
    for word in text:
        y.append(ps.stem(word))
        
    return " ".join(y)

try:
    Tfidf = pickle.load(open('Vectorizer.pkl', 'rb'))
    model = pickle.load(open('model.pkl', 'rb'))
except FileNotFoundError as e:
    st.error(f"Error: {e}")


st.title(" 📩 Email/SMS Spam Classifiers")
input_Sms=st.text_area("Enter the message")

#Button
if st.button('predict'):
 
 # Preprosissing
    transformed_sms= transform_text(input_Sms)

# Vectorize
    vector_input = Tfidf.transform([transformed_sms])

#Pridict
    result=model.predict(vector_input)[0]

# Display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")
        