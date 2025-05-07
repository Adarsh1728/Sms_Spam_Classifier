import pickle
import streamlit as st
from win32com.client import Dispatch
import pythoncom

# Function to speak the result
def speak(text):
    try:
        pythoncom.CoInitialize()
        speak_engine = Dispatch("SAPI.SpVoice")
        speak_engine.Speak(text)
        pythoncom.CoUninitialize()
    except Exception as e:
        print(f"Text-to-speech error: {e}")

# Load model and vectorizer safely
try:
    with open("model.pkl", "rb") as model_file, open("Vectorizer.pkl", "rb") as vectorizer_file:
        model = pickle.load(model_file)
        Vectorizer = pickle.load(vectorizer_file)
except Exception as e:
    st.error(f"Failed to load model/vectorizer: {e}")
    st.stop()

# Streamlit App
def main():
    st.title("📧 Email Spam Classifier")
    st.subheader("Built with Streamlit & Python")

    msg = st.text_area("Enter a message:")

    if st.button("Predict"):
        if not msg.strip():
            st.warning("Please enter a message.")
            return

        try:
            # Ensure vectorizer exists before transformation
            if Vectorizer:
                data = [msg]
                vect = Vectorizer.transform(data).toarray()
                prediction = model.predict(vect)
                result = prediction[0]

                # Display result
                if result == 1:
                    st.header("🚫 Spam")
                    speak("It's Spam.")
                else:
                    st.header("✅ Not Spam")
                    speak("It's not Spam.")
            else:
                st.error("Vectorizer is not initialized properly.")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# Run the app
if __name__ == "__main__":
    main()
