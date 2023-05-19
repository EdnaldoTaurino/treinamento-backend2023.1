print('-'*80)
print('-'*40, 'ENERGISA', '-'*30)
print('-'*80)

kwh = float(input('Qual a quantidade de kilowatts ?: '))
tipo = input('Qual tipo de instalação  "R" "I" ou "C": ').lower()


if tipo == 'r' and kwh <= 500:
    valor = kwh * 0.40
    print(f'O valor a pagar de energia eletrica é de: {valor}')
elif tipo == 'r' and kwh > 500:
    valor = kwh * 0.65
    print(f'O valor a pagar de energia eletrica é de: {valor}')

if tipo == 'i' and kwh <= 500:
    valor = kwh * 0.40
    print(f'O valor a pagar de energia eletrica é de: {valor}')
elif tipo == 'i' and kwh > 500:
    valor = kwh * 0.90
    print(f'O valor a pagar de energia eletrica é de: {valor}')

else:
    print('Escolha uma opção valida FIM DO PROGRAMA!!!')
