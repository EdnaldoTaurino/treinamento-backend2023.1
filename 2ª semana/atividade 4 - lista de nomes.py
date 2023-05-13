# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a
# maioridade e quantas já são maiores

# input nomes ano de nascimento \ contador de nomes maior idade++ \ if idade > 18 contador idade ++ else menor idade++

from datetime import date
ano_atual = date.today().year

maior_idade = 0
menor_idade = 0

for i in range(2):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior_idade += 1
    else:
        menor_idade += 1

print(f'''
{maior_idade} pessoas maior de idade
{menor_idade} pessoas menor de idade''')
