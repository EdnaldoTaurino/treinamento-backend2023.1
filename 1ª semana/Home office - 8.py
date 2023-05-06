# Faça um programa que mude uma palavra da String "treinamento hoje de backend capturando do teclado duas palavras:
# a que deverá ser trocada por qual palavra
frase = 'Treinamento hoje de backend'
print('Treinamento hoje de backend')
palavra_antiga = input('Digite a palavra que deseja substituir: ')
palavra_nova = input('Digite a palavra que irá substituir a palavra anterior: ')

nova_frase = frase.replace(palavra_antiga, palavra_nova)

print(f'A nova frase é: {nova_frase}')
