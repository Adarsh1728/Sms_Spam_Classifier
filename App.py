import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK stopwords
nltk.download('stopwords')

ps = PorterStemmer()

def transform_text(text):
    text = text.lower()
    text = text.split()
    y = [word for word in text if word.isalnum()]
    y = [ps.stem(word) for word in y if word not in stopwords.words('english') and word not in string.punctuation]
    return " ".join(y)

# Load model and vectorizer
try:
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("Vectorizer.pkl", "rb") as vect_file:
        vectorizer = pickle.load(vect_file)
except Exception as e:
    st.error(f"Error loading model/vectorizer: {e}")
    st.stop()

st.set_page_config(page_title="SMS Spam Classifier", layout="centered")
st.title("📩 SMS/Email Spam Classifier")

input_sms = st.text_area("Enter your message:", height=150)

if st.button("Predict"):
    if not input_sms.strip():
        st.warning("Please enter a message.")
    else:
        transformed_sms = transform_text(input_sms)
        vector_input = vectorizer.transform([transformed_sms])
        prediction = model.predict(vector_input)[0]
        if prediction == 1:
            st.error("❌ Spam")
        else:
            st.success("✅ Not Spam")
