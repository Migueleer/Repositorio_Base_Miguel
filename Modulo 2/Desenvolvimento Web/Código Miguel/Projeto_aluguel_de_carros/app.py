import streamlit as st
#python -m streamlit run app.py

# aqui é o primordial, sempre precisamos criar o servidor

#aqui coloca titulo
st.title('Olá, Mundo, sou programador')

#criando um calendário
date = st.date_input("Selecione uma data")

#Permitindo o upload do arquivo
file = st.file_uploader("Salveee")