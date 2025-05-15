import streamlit as st
import pickle
import re
import string

# 1. Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# 2. Function to preprocess input text
def preprocess_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    return text

# 3. Streamlit App
st.set_page_config(page_title="Spam Detection App", page_icon="📩")

st.title("📩 Spam Detection App")
st.write("Enter your message below and I'll tell you if it's Spam or Not Spam!")

user_input = st.text_area("Enter a message:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message.")
    else:
        cleaned_input = preprocess_text(user_input)
        vectorized_input = vectorizer.transform([cleaned_input])
        prediction = model.predict(vectorized_input)[0]

        if prediction == 1:
            st.error("🚨 Spam Message Detected!")
        else:
            st.success("✅ Not a Spam Message!")
