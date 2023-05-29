# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. (OK)
# Calcule o valor da prestação mensal, sabendo que não pode exceder 30% do salário ou então o emprestimo será negado.

casa = float(input('Qual valor da casa? R$ '))
salario = float(input('Qual seu salário? R$ '))
anos = int(input('Em quantos anos deseja pagar a casa? '))

meses = anos * 12
prestacao = casa / meses
salario30 = salario * 30/100

if prestacao <= salario30:
    print('Emprestimo aprovado! ')

else:
    print('Rejeitado!')