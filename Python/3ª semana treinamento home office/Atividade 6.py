# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os
# valores
# ímpares digitados, respectivamente. Ao final mostre o conteúdo das tres
# listas
# geradas.

# Criando a lista principal
numeros = []

# Criando as listas extras
pares = []
impares = []

# Lendo os números do usuário e adicionando-os à lista principal
while True:
    numero = int(input("Digite um número (ou 0 para sair): "))

    if numero == 0:
        break

    numeros.append(numero)

    # Classificando os números em pares ou ímpares
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# Exibindo o conteúdo das três listas
print("Lista principal:", numeros)
print("Lista de números pares:", pares)
print("Lista de números ímpares:", impares)
