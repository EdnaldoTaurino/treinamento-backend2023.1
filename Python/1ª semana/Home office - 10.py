# faça um programa que verifique se uma palavra está dentro da string e retorne true ou false

palavra = (input('Digite uma frase: '))
frase = input('Digite uma palavra para verificar se esta dentro da frase: ')

if frase in palavra:
    print('Verdadeiro')
else:
    print('Falso')