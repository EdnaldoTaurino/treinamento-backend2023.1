# Crie um programa que faça o computador jogar Pedra, Papel e Tesoura

import random  # from random import randint
import time
opcoes = ['Pedra', 'Papel', 'Tesoura']

usuario = int(input('''
1 - pedra
2 - Papel
3 - Tesoura
:'''))

if usuario < 1 or usuario > 3:
    print('Opção inválida')
else:
    computador = random.randint(1, 3)
    print('''
    Pedra papel e''')
    time.sleep(1)
    print('''TESOURAAAAAAAAAA!!!''')
    time.sleep(1)
# como lista começa com 0 teve que colocar -1 aqui lista começa com 0pedra, 1papel, 2tesoura -1 o computador escolhe
    print(f'O computador escolheu {opcoes[computador-1]}')  # corretamente se tirar ele escolhe errado

if usuario == computador:  # " if usuario == computador+1: " assim também dava certo aqui
    print('Empate!!!')

elif usuario == 0 and computador == 1 or usuario == 1 and computador == 0 or usuario == 2 and computador == 1:
    print('Você venceu!!!')

else:
    print('Computador venceu')