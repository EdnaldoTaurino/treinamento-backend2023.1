# Criar um programa que digite o nome de varios alunos e sortei um.

import random
alunos = []
novo_aluno = "Ninguem"
sorteado = "sortudo"
while novo_aluno != "0":
    novo_aluno = str(input('Vamos descobrir quem é o aluno sorteado. (digite 0 para parar o sorteio). Digite o nome da pessoa: '))
    if novo_aluno == '0':
        break
    alunos.append(novo_aluno)
if alunos != []:
    sorteado = random.choice(alunos)
    print(f"{sorteado} foi o sorteado")
else:
    print("Lista vazia")