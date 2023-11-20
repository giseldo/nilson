import streamlit as st
from chatbot import respond

st.title("💬 Chatbot Nilson")
st.caption("🚀 Um chatbot para auxiliar o escritorio LPD")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Como posso te ajudar?"}]
    st.chat_message("assistant").write("Voce pode pedir para eu contar uma piada, posso informar nosso endereço ou você pode solicitar informações do seu processo")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
    

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = respond(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)