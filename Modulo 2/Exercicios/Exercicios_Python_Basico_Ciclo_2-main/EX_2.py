# Utilize um loop while e um loop for para percorrer a lista e exibir os valores dos items contidos na lista

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

frutas = ['maçã', 'banana', 'morango', 'uva', 'laranja']

# LOOP WHILE
print("Com WHILE:")
i = 0
while i < len(frutas):
    print(frutas[i])
    i += 1

# LOOP FOR
print("\nCom FOR:")
for fruta in frutas:
    print(fruta)