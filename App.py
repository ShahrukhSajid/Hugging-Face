import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

# Load the translation model and tokenizer
model_name = "HaiderSultanArc/t5-small-english-to-urdu"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
translator = pipeline("translation_en_to_ur", model=model, tokenizer=tokenizer)

# Streamlit UI
st.title("English to Roman Urdu Translator")

# Input text box
input_text = st.text_area("Enter English text:")

# Translation button
if st.button("Translate"):
    if input_text:
        translated_text = translator(input_text)[0]['translation_text']
        st.write("**Translated Text:**")
        st.write(translated_text)
    else:
        st.error("Please enter some text to translate.")
