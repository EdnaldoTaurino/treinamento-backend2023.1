# Faça um programa que leia, nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - a média de idade do grupo.
# - qual é o nome do homem mais velho.
# - quantas mulheres tem menos de 20 anos

soma_idades = 0
qtd_mulheres20 = 0
homem_mais_velho = ''
maior_idade_homem = 0


for i in range(4):
    print(f'Digite os dados da {i+1} pessoa: ')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo M ou F: ').upper()

    # Soma a idade de todas as pessoas
    soma_idades += idade

    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome

    if sexo == 'F' and idade < 20:
        qtd_mulheres20+=1

media = soma_idades/4

print(f'''
O mais homem mais velho foi {homem_mais_velho}
A média das idades é de {media}
A quantidade de mulheres menor que 20 anos: {qtd_mulheres20}''')