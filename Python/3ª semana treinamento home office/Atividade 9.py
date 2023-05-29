# Faça um programa que leia nome e média de um aluno, guardando também a
# solução
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.


aluno = {}

aluno['nome'] = input("Digite o nome do aluno: ")
aluno['media'] = float(input("Digite a média do aluno: "))

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")




# outra forma de fazer o codigo
aluno = {
    'nome': input("Digite o nome do aluno: "),
    'media': float(input("Digite a média do aluno: "))
}

print("\nDados do aluno:")
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
