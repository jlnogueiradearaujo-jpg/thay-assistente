import streamlit as st
from transformers import pipeline

# Título do app
st.set_page_config(page_title="Thay - Assistente da Calçados 24h", page_icon="👟")
st.title("👟 Thay - Assistente Virtual da Calçados 24h")

# Carrega o modelo (só uma vez, cacheado)
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="nomic-ai/gpt4all-j")

generator = load_model()

# Histórico de conversa
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Exibir mensagens anteriores
for msg in st.session_state["messages"]:
    st.markdown(f"**{msg['role']}:** {msg['content']}")

# Entrada do usuário
user_input = st.text_input("Digite sua mensagem:")

if user_input:
    st.session_state["messages"].append({"role": "Você", "content": user_input})
    response = generator(user_input, max_length=200, do_sample=True, temperature=0.7)[0]["generated_text"]
    st.session_state["messages"].append({"role": "Thay", "content": response})
    st.experimental_rerun()
