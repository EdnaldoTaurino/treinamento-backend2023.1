#faça um programa que diga se o numero é par ou impar

numero = float (input('Digite um numero para saber se é par ou imprar '))
resto = numero % 2 # % RESTO DA DIVISÃO

if resto ==0:
    print('o numero {:.0f} é par' .format(numero) )  #{:.of} diz que não quero zeros apos o número, COMO CONVERTER PARA VIRGULA E DINHEIRO?

else:
    print('Número é impar')