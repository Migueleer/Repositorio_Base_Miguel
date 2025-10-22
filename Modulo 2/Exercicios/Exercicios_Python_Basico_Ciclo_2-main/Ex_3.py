# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista

# LOOP WHILE
quantidade = int(input("Quantos filmes deseja adicionar na lista?"))
print("\nAdicionando com WHILE:")
i = 0 
while i < quantidade:
    nome = input(f"Digite o nome do {i+1}º filme:")
    filmes.append(nome)
    i += 1

    print("\nLista de filmes adicionados (while):")
print(filmes)

# LOOP FOR
filmes = []
print("\nAdicionando com FOR:")
for i in range(quantidade):
    nome = input(f"Digite o nome do {i+1}º filme:")
    filmes.append(nome)

print("\nLista de filmes adicionados com (for):")
print(filmes)

