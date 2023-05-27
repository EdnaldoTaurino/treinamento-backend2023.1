# Faça um programa que ajude um jogador da MEGA SENA a criar papites. O
# programa
# vai perguntar quantos jogos serão gerados e vai sortear 5 números entre 1 e 50
# para
# cada jogo, cadastrando tudo em uma lista composta

import random

# Obtendo a quantidade de jogos a serem gerados
quantidade_jogos = int(input("Quantos jogos deseja gerar? "))

# Gerando os jogos
jogos = []
for _ in range(quantidade_jogos):
    jogo = random.sample(range(1, 51), 5)
    jogos.append(jogo)

# Exibindo os jogos gerados
print("Jogos gerados:")
for jogo in jogos:
    print(jogo)
