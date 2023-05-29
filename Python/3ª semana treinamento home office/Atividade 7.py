# crie um programa onde o usuário possa digitar 5 valores numéricos e cadastreos
# em uma lista única que mantenha separados os valores pares e impares. No final,
# mostre os valores pares e impares em ordem crescente

# Criando a lista única
numeros = []

# Lendo os valores do usuário e adicionando-os à lista
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(valor)

# Separando os valores pares e ímpares
pares = sorted([num for num in numeros if num % 2 == 0])
impares = sorted([num for num in numeros if num % 2 != 0])

# Exibindo os valores pares em ordem crescente
print("Valores pares em ordem crescente:", pares)

# Exibindo os valores ímpares em ordem crescente
print("Valores ímpares em ordem crescente:", impares)
