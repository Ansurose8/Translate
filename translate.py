import streamlit as st
from googletrans import Translator

st.header ('Machine Translation Demo')
input = st.text_area("Enter text to text",value="")
option = st.selectbox(
    'To which language you want to translate the text to?',
    ('Malayalam','Hindi','Tamil'))

if st.button('Translate'):
    translator = Translator()
    translation = translator.translate(input,dest=option)
    st.write(translation.text)
