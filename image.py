import streamlit as st
from text_summarisation import generate_summary as gs
import easyocr

img_obj = easyocr.Reader(['en'])

st.title("Text Summarisation using NLP")
st.text("The model uses pagerank algorithm and cosine similarity for extractive summarisation.")
value = st.file_uploader("Upload the image containing the text.")
top_n = st.number_input("Enter the number of important lines you require")
summary = gs(value, int(top_n))
result = st.button("Summarize")
if result:
    st.write(summary)