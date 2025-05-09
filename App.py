import pickle
from flask import Flask, render_template, request, jsonify
from win32com.client import Dispatch
import pythoncom
from flask_cors import CORS
# Use correct folder name for templates
App = Flask(__name__)
CORS(App)

# Function to speak the result using Windows speech
def speak(text):
    try:
        pythoncom.CoInitialize()
        speaker = Dispatch("SAPI.SpVoice")
        speaker.Speak(text)
        pythoncom.CoUninitialize()
    except Exception as e:
        print(f"Text-to-speech error: {e}")

# Load model and vectorizer
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load data
df = pd.read_csv("spam.csv", encoding="latin-1")[["v1", "v2"]]
df.columns = ["label", "text"]
df["label_num"] = df.label.map({"ham": 0, "spam": 1})

# Vectorization
Vectorizer = CountVectorizer()
X = Vectorizer.fit_transform(df["text"])
y = df["label_num"]

# Train model
model = MultinomialNB()
model.fit(X, y)

# Save model and vectorizer
with open("model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)

with open("Vectorizer.pkl", "wb") as vect_file:
    pickle.dump(Vectorizer, vect_file)

print("Model and Vectorizer saved successfully.")
    
# Home route
@App.route("/")
def home():
    return render_template("index.html")  # Make sure index.html is inside /templates

# Prediction route
@App.route("/predict", methods=["POST"])

@App.route('/api', methods=['POST'])
def api_predict():
    data = request.get_json()
    msg = data.get('message', '')
    if not msg:
        return jsonify({'result': 'No message received'}), 400

    vect = Vectorizer.transform([msg]).toarray()
    prediction = model.predict(vect)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    speak(f"It's {result}.")
    return jsonify({'result': result})

# Run app
if __name__ == "__main__":
    App.run(debug=True)
