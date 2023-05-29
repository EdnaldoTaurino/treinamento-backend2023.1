# Crie um programa onde 4 jogadores joguem um dado e tenham resultados
# aleatórios.
# Guarde esses resultados em um dicionário. No final, coloque esse dicionário em
# ordem,
# sabendo que o vencedor tirou o maior número no dado.

import random

jogadores = {}

for c in range(1, 5):
    nome = input(f"Nome do jogador {c}: ")
    dado = random.randint(1, 6)
    jogadores[nome] = dado

jogadores_ordenados = sorted(jogadores.items(), key=lambda x: x[1], reverse=True)

print("Resultado do jogo:")
for jogador, resultado in jogadores_ordenados:
    print(f"Jogador: {jogador} - Resultado: {resultado}")

vencedor = jogadores_ordenados[0][0]
print(f"O vencedor é: {vencedor} que tirou o maior numero no dado numero: {dado}")
