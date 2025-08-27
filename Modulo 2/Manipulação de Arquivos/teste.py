# criar 2 listas, nome carros, com 4 carros, segunda lista, preço aluguel vai ter os valores do aluguel
#pedir pro usuario o nome do carro q ele quer alugar e quantos dias ele quer alugar
# calcular quanto vai gastar de aluguel


carros = ["civic","i30","corolla","fox"]
preco_aluguel = [150, 100, 125, 80]

print("Carros disponíveis para alugar:")
for i in range(len(carros)):
    print(f"{i+1} - {carros[i]} (R${preco_aluguel[i]} por dia)")

carro_escolhido = input("Digite o nome do carro que deseja alugar:")
dias = int(input("Quantos dias você quer alugar?"))

if carro_escolhido in carros:
    indice = carros.index(carro_escolhido)
    total = preco_aluguel[indice] * dias 
    print(f"Você vai gastar R${total} para alugar o {carro_escolhido} por {dias} dias.")
else:
    print("Carro não encontrado.")   