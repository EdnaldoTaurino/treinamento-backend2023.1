# Crie um programa que calcule o valor a ser pago por produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/pix: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

produto = float(input('Digite o preço do produto: R$ '))
print('''
1 - à vista dinheiro/pix: 10% de desconto
2 - à vista no cartão: 5% de desconto
3- em até 2x no cartão: preço normal
4- 3x ou mais no cartão: 20% de juros''')

opcao = int(input('Escolha qual opção de 1 a 4: '))

if opcao == 1:
    produto = produto - (produto * 10/100)  # ou produto = produto * 0.9
    print(f'Desconto de 10% total do produto foi de: R$ {produto}')

elif opcao == 2:
    produto = produto - (produto * 5/100)  # ou produto = produto * 0.5
    print(f'O produto teve um desconto de 5% total de: R$ {produto}')

elif opcao == 3:
    print(f'O preco normal do item está por R$ {produto}')

elif opcao == 4:
    parcela = int(input('Digite o numero de parcelas: '))
    produto = produto + (produto * 20/100)  # ou produto = produto * 0.95
    parcela = produto / parcela
    print(f'No cartão com acrescimo de 20% total de: R$ {produto} e as parcelas total de: R$ {parcela} por parcela')

else:
    print('Escolha uma opção válida')