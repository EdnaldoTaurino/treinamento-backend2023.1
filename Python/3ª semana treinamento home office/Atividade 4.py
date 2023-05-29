# faça um programa que leia 5 valores números e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e suas
# respectivas posições na lista

# Criando a lista vazia
numeros = []

# Lendo os valores do usuário e adicionando-os à lista
for i in range(5):
    valor = int(input(f"Digite o {i+1}º valor: "))
    numeros.append(valor)

# Encontrando o maior valor e sua posição
maior_valor = max(numeros)
posicao_maior = numeros.index(maior_valor)

# Encontrando o menor valor e sua posição
menor_valor = min(numeros)
posicao_menor = numeros.index(menor_valor)

# Exibindo os resultados
print("Valores digitados:", numeros)
print("Maior valor:", maior_valor, "| Posição:", posicao_maior)
print("Menor valor:", menor_valor, "| Posição:", posicao_menor)
