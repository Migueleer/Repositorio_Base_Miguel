import streamlit as st
import requests
import json
import BuscarCep
import pandas as pd


##### TÍTULO DA APLICAÇÃO #####
st.title("Busca CEP")



##### Imagem e Título #####
st.sidebar.image("logo.png")
st.sidebar.title("Busca CEP")
st.sidebar.markdown('Aplicação para buscar endereço a partir do CEP e mostrar a localização no mapa.')

# opções na sidebar
opcoes = ["Buscar CEP", "Descobrir CEP"]
opcao = st.sidebar.selectbox("Escolha uma opção:", opcoes)
##### BARRA LATERAL #####


##### BOTÃO BUSCAR CEP #####
if opcao == 'Buscar CEP':
    st.image('principal.png')
    st.subheader('Buscar Endereço pelo CEP')
    cep = st.text_input('Digite o CEP(somente números):')
    # st.button('Buscar')

# if opcao == "Buscar CEP":
#     st.header("Buscar Endereço pelo CEP")
#     cep = st.text_input("Digite o CEP (somente números):")

    if st.button("Buscar"):
        if len(cep) != 8 or not cep.isdigit():
            st.error("Por favor, insira um CEP válido com 8 digitos númericos.")
        else:
            try:
                endereco = BuscarCep.buscar_cep(cep)
                if endereco:
                    st.success("Endereço encontrado:")
                    st.write(f"CEP: {endereco[0]}")
                    st.write(f"Endereço: {endereco[1]}")
                    st.write(f"Bairro: {endereco[2]}")
                    st.write(f"Cidade: {endereco[3]}")
                    st.write(f"Estado: {endereco[4]}")

                    ## Mapas
                    st.title("Localização no Mapa")
                    df = pd.DataFrame({"latitude": [endereco[5]], "longitude": endereco[6]})
                    st.map(df, zoom=15)
                else:
                    st.error("CEP não encontrado")
            except Exception as e:
                st.error(f"Ocorreu um erro ao buscar o CEP: {e}")




##### BOTÃO DESCOBRIR CEP #####
elif opcao == 'Descobrir CEP':
    st.image('Descobrir.png')
    st.subheader('Buscar CEP pelo endereço')
    endereco_usuario = st.text_input('Digite seu endereço (ex: Rua Olga, Barueri, SP):')
    # st.button('Descobrir')

    if st.button("Descobrir"):
        if not endereco_usuario.strip():
            st.error("Por favor, insira um endereço válido.")
        else:
            try:
                resultado = BuscarCep.descobrir_cep(endereco_usuario)
                st.success("Link de busca no Google:")
                st.write(resultado)
            except Exception as e:
                st.error(f"Ocorreu um erro ao descobrir o CEP: {e}")
                

















