# Cria as variáveis necessárias
soma_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
quantidade_mulheres_menos_20 = 0

# Faz um loop para ler os dados das 4 pessoas
for i in range(2):
    print(f'--- {i+1}ª PESSOA ---')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()  # deixa todas as letras maiúscula independente de como digitar

    # Soma a idade de todas as pessoas
    soma_idade += idade

    # Verifica se é homem e se é o mais velho
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome

    # Verifica se é mulher e tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        quantidade_mulheres_menos_20 += 1

# Calcula a média de idade do grupo
media_idade = soma_idade / 4

# Exibe os resultados
print(f'A média de idade do grupo é {media_idade:.1f} anos.')
print(f'O homem mais velho é o {nome_mais_velho} com {maior_idade_homem} anos.')
print(f'{quantidade_mulheres_menos_20} mulher(es) tem menos de 20 anos.')
