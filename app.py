import streamlit as st
from transformers import pipeline

# Título
st.title("🤖 Thay - Assistente da Calçados 24h")

# Carrega modelo
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="nomic-ai/gpt4all-j")

generator = load_model()

# Entrada do usuário
user_input = st.text_input("Digite sua mensagem para a Thay:")

if user_input:
    response = generator(user_input, max_length=200, do_sample=True, temperature=0.7)[0]['generated_text']
    st.write("**Thay:**", response)
