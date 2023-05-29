nomes = []
for i in range(7):
    nome = input('Digite seu nome: ')
    nomes.append(nome)

#####################################3333
from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for i in range(7):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {i+1}ª pessoa: '))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Total de maiores de idade: {maiores}')
print(f'Total de menores de idade: {menores}')


###################################################
