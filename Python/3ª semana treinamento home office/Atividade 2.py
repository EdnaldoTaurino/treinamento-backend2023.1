# crie um programa q vai gerar cinco números aleatórios e colocar
# em uma tupla.
# depois disso, mostre a listagem de numeros gerados e também
# indique o menor e
# e o maior valor que estao na tupla

import random

# Gerando cinco números aleatórios e colocando em uma tupla
numeros_aleatorios = tuple(random.sample(range(1, 101), 5))

# Exibindo a listagem de números gerados
print("Números gerados:", numeros_aleatorios)

# Obtendo o menor valor da tupla
menor_valor = min(numeros_aleatorios)

# Obtendo o maior valor da tupla
maior_valor = max(numeros_aleatorios)

# Exibindo o menor e o maior valor
print("Menor valor:", menor_valor)
print("Maior valor:", maior_valor)
