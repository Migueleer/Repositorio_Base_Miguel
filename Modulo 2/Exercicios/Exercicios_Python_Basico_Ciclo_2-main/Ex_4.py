# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']
notas = [float(nota) for nota in notas]

# LOOP WHILE
i = 0
soma = 0 
while i < len(notas):
    soma += notas[i]
    i += 1
media_while = soma / len(notas)
print("Média com while:", media_while)

# LOOP FOR
soma = 0
for nota in notas:
    soma += nota
media_for = soma / len(notas)
print("Média com for:", media_for)





