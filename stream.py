import streamlit as st
from text_summarisation import generate_summary as gs

value = ''
st.title("Text Summarisation using NLP")
st.text("The model uses pagerank algorithm and cosine similarity for extractive summarisation.")
# st.selectbox("Source of the text::", ['URL','Text entered manually', 'File (.txt, .pdf, .doc)'])
docNum = st.number_input("Enter the number of documents")
value = st.text_input("Enter the text for summarisation")
top_n = st.number_input("Enter the number of important lines you require")
summary = gs(value, int(top_n))
sumText = summary.split('.')
result = st.button("Summarize")
if result:
     for i in sumText:
          st.write('-->', i, '\n')

