# Crie uma lista com 3 dicionários, cada um representando uma pessoa (contendo nome, idade, cidade). Use um laço para imprimir o nome de cada pessoa.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
pessoas = [
    {"nome": "Miguel", "idade": 18, "cidade": "São Paulo"}, 
    {"nome": "Kaio", "idade": 17, "cidade": "Minas Gerais"},
    {"nome": "Mateus", "idade": 24, "cidade": "Rio de Janeiro"}
]

for pessoa in pessoas:
    print(pessoa["nome"])
