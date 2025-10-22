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
st.sidebar.title('Miguel Games')

jogos = ['GTA V', 'GTA IV', 'GTA San Andreas', 'CoD Black Ops', 'CoD Black Ops 2', 'Need for Speed Most Wanted', 'Gran Turismo 4', 'EA fc 26', 'God of War 3', 'God of War Ragnarok', 'Dead Space', 'Dead Space 2', 'Dead Space 3', 'Max Payne', 'Max Payne 2', 'Max Payne 3']
valor = [118.91, 80, 198.90, 60.90, 105, 34.90, 179.91, 338, 80, 249.90, 249.93, 209.87, 159.90, 84.90, 84.90, 104.90]


opcao = st.sidebar.selectbox('Escolha o jogo que deseja comprar', jogos)
# opcao_jogos = st.sidebar.selectbox('Preço', valor)

indice = jogos.index(opcao)
custo = valor[indice]

# Principal
st.title('Miguel Games - Venda de Jogos')

st.image(f'{opcao}.png')
st.markdown(f'## Você deseja comprar o jogo: {opcao} por apenas: R$ {custo:.2f}')
st.markdown('---')

quantidade_comprada = st.text_input(f'Quantos produtos você deseja comprar?')


frete = 15

if opcao == 'GTA V':
    preco = 188.91

elif opcao == 'GTA IV':
    preco = 80

elif opcao == 'GTA San Andreas':
    preco = 198.90

elif opcao == 'CoD Black Ops':
    preco =  60.90

elif opcao == 'CoD Black Ops 2':
    preco =  105

elif opcao == 'Need for Speed Most Wanted':
    preco =  34.90

elif opcao == 'Gran Turismo 4':
    preco = 179.91

elif opcao == 'EA fc 26':
    preco = 338

elif opcao == 'God of War 3':
    preco = 80

elif opcao == 'God of War Ragnarok':
    preco = 249.90

elif opcao == 'Dead Space':
    preco = 249.93

elif opcao == 'Dead Space 2':
    preco = 209.87

elif opcao == 'Dead Space 3':
    preco = 159.90

elif opcao == 'Max Payne':
    preco = 84.90

elif opcao == 'Max Payne 2':
    preco = 84.90

elif opcao == 'Max Payne 3':
    preco = 104.90 

if st.button('Comprar'):
    quantidade_comprada = int(quantidade_comprada)
    valor_total = quantidade_comprada * preco + frete

    st.warning(f'Você comprou o jogo: {opcao},  por R${valor_total:.2f}')




