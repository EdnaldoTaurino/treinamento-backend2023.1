# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
# por extenso, de zero até dez.
# seu programa deverá ler um número pelo teclado (entre 0 e 10) e mostrá-lo
# por extenso


# Definindo a tupla com os números por extenso
numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro','cinco', 'seis', 'sete', 'oito', 'nove', 'dez')

# Solicitando um número ao usuário
numero = int(input("Digite um número entre 0 e 10: "))

# Verificando se o número está dentro do intervalo válido
if 0 <= numero <= 10:
    # Imprimindo o número por extenso
    print("Número por extenso:", numeros_extenso[numero])
else:
    print("Número inválido. Tente novamente.")
