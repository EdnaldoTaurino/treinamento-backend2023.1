# Faça um programa que o usuário informe o salário recebido e o total gasto em despesas.
# Deverá ser exibido na tela "Gastos dentro do orçamento" se o valor gasto não ultrapassar o valor do salário

salario = float(input('Informe seu salário: R$ '))
despesas = float(input('Quanto foi gasto com despesas? : R$ '))

if despesas >= salario:
    print('Você gastou mais do que deveria')
else:
    print('Gastos dentro do orçamento')