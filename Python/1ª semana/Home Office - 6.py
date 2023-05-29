# faça um programa que peça o ano de nascimento do usuário e verifique se ele é maior ou menor de idade, mostrando a
# idade calculada

# lendo variaveis
idade = int(input('Qual ano do seu nascimento? '))
maior_idade = 2023 - idade  # Calculando idade refente ao ano atual

print(f'sua idade é {maior_idade}')

if maior_idade >= 18:
    print('Você é maior de idade ')
else:
    print('Você é menor de idade')


