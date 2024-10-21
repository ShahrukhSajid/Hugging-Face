import streamlit as st
from transformers import pipeline

# Load the translation model
translator = pipeline("translation", model="HuggingFaceModelName")  # Replace with your model name

st.title("English to Roman Urdu Translator")

input_text = st.text_area("Enter English text:")

if st.button("Translate"):
    if input_text:
        translation = translator(input_text, target_lang="ur")[0]['translation_text']  # Modify as needed
        st.write("Translation:", translation)
    else:
        st.write("Please enter some text to translate.")

