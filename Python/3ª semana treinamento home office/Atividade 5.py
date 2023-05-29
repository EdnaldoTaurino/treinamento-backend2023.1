# Crie um programa onde o usuário possa digitar cinco valores númericos
# e cadastre-os em uma lista, já na posição correta de inserção. No final,
# mostre a lista ordenada na tela.

# Criando a lista vazia
numeros = []

# Lendo os valores do usuário e inserindo-os na posição correta
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))

    if i == 0:
        numeros.append(valor)
    else:
        posicao = 0
        while posicao < len(numeros) and valor > numeros[posicao]:
            posicao += 1
        numeros.insert(posicao, valor)

# Exibindo a lista ordenada
print("Lista ordenada:", numeros)
