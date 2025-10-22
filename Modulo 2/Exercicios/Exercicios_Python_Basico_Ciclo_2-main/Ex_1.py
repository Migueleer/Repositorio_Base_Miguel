# Utilize um loop while e um loop for para contar de 0 até o número que o usuário digitar:

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
numero = int(input("Digite um número:"))

# LOOP WHILE
print("\n Contagem com WHILE:")
contador = 0 
while contador <= numero:
    print(contador)
    contador += 1

# LOOP FOR
print("\n Contador com FOR:")
for i in range(0, numero + 1):
    print(i)


