import streamlit as st
from transformers import pipeline

# Load the translation model
# Replace 'your-model-name' with the actual model from Hugging Face that supports English to Roman Urdu translation
model_name = "your-model-name"  # e.g., "HuggingFaceH4/your-model"
translator = pipeline("translation", model=model_name)

# Streamlit app layout
st.title("English to Roman Urdu Translator")

input_text = st.text_area("Enter English text:")

if st.button("Translate"):
    if input_text:
        # Perform translation
        translation = translator(input_text, target_lang="ur")[0]['translation_text']
        st.write("Translation:", translation)
    else:
        st.write("Please enter some text to translate.")
