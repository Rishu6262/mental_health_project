import streamlit as st
import joblib
import re

# Load model and vectorizer
model = joblib.load("mental_health_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    return text

# App Title
st.set_page_config(page_title="Mental Health Predictor", layout="centered")

st.title("🧠 Mental Health Prediction App")
st.markdown("Predict **mental health condition** from user text using **Machine Learning (NLP)**")

st.divider()

# User Input
user_input = st.text_area(
    "✍️ Enter your thoughts / text here:",
    height=150,
    placeholder="Example: I feel anxious and stressed these days..."
)

# Predict Button
if st.button("🔍 Predict Mental Health Status"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter some text first!")
    else:
        cleaned_text = clean_text(user_input)
        vector = tfidf.transform([cleaned_text])
        prediction = model.predict(vector)[0]

        st.success(f"✅ Predicted Mental Health Condition: **{prediction}**")

st.divider()

# Footer
st.markdown(
    """
    👨‍💻 **Project Type:** NLP Text Classification  
    📌 **Model Used:** TF-IDF + SVM  
    🚀 **Built with Streamlit**
    """
)
