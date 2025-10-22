import streamlit as st

st.title("Calcular Média")


nota1 = st.text_input("Digite a primeira nota")
nota2 = st.text_input("Digite a segunda nota")
nota3 = st.text_input("Digite a terceira nota")
nota4 = st.text_input("Digite a quarta nota")



if st.button("Calcular média"):
    nota_1 = float(nota1)
    nota_2 = float(nota2)
    nota_3 = float(nota3)
    nota_4 = float(nota4)

    media = (nota_1 + nota_2 + nota_3 + nota_4)/4

    if media >= 7.0:
        st.warning(f"Você ficou com a média: {media:.2f}, Parabéns você foi aprovado✅")

    elif media >= 5.0 and media <= 7.0:
        st.warning(f"Você ficou com a média: {media:.2f}, você ficou de recuperação⚠️")

    elif media < 5.0:
        st.warning(f"Você ficou com a média: {media:.2f}, você foi reprovado❌")