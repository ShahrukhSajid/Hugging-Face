import streamlit as st
from transformers import pipeline

# Load the translation model from Hugging Face
model_name = "HuggingFace-username/model-name"  # Replace with your model's name
translator = pipeline("translation_en_to_roman_ur", model=model_name)

# Streamlit UI
st.title("English to Roman Urdu Translator")

# Input text box
input_text = st.text_area("Enter English text:")

# Translation button
if st.button("Translate"):
    if input_text:
        # Translate the input text
        translated_text = translator(input_text)[0]['translation_text']
        st.write("**Translated Text:**")
        st.write(translated_text)
    else:
        st.error("Please enter some text to translate.")
