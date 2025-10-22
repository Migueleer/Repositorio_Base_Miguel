# import streamlit as st
# #python -m streamlit run app.py

# # aqui é o primordial, sempre precisamos criar o servidor

# #aqui coloca titulo
# st.title('Olá, Mundo, sou programador')

# #criando um calendário
# date = st.date_input("Selecione uma data")

# #Permitindo o upload do arquivo
# file = st.file_uploader("Salveee")

import streamlit as st
import pandas as pd 

# Sidebar
st.sidebar.image("logo.png")
st.sidebar.title('Miguel Motors')

carros = ['Lancer', 'Civic', 'Corolla', 'Golf TSi', 'Jetta', 'Celta', 'Hilux', 'Corsa', 'Blazer', 'Punto']

opcao = st.sidebar.selectbox('Escolha o carro que foi alugado', carros)


# Principal
st.title('Car Future - Aluguel de Carros')

st.image(f'{opcao}.png')
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f'Por quantos dias o {opcao} foi alugado?')
km = st.text_input(f'Quantos kms você rodou com o {opcao}?')

if opcao == 'Lancer':
    diaria = 350

elif opcao == 'Civic':
    diaria = 300

elif opcao == 'Corolla':
    diaria = 250

elif opcao == 'Golf TSi':
    diaria = 500

elif opcao == 'Jetta':
    diaria = 250

elif opcao == 'Celta':
    diaria = 100

elif opcao == 'Hilux':
    diaria = 150

elif opcao == 'Corsa':
    diaria = 175

elif opcao == 'Blazer':
    diaria = 240

elif opcao == 'Punto':
    diaria = 200
























if st.button('Calcular'):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria
    total_km = km * 0.15
    aluguel_total = total_dias+total_km

    st.warning(f'Você alugou o {opcao} por {dias} e rodou {km} km. O valor total a pagar é R${aluguel_total:.2f}')




