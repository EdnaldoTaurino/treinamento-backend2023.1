#ler três numeros e dizer: sao diferentes ou iguais

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o terceiro número: '))

if numero1 == numero2 == numero3:
    print('Os números são iguais')

elif numero1 == numero2 != numero3:
    print('Dois números iguais')

elif numero1 != numero2 == numero3:
    print('dois numeros são iguais')

else:
    print('Todos os números são diferentes')