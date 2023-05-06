#faça um programa que peça 5 números e informe o maior deles (OK)
#criando um problema: a pessoa digite quantos números quiser e só para quando digitar a palavra pare ou o número 0
#e informe o maior número e o maior número digitado

#-------------------------------------------------------------------------------------------------------------------------------------------

#o TRY tentar converter a entrada do usuário para um número inteiro. Se a conversão for bem sucedida, 
#o código continua normalmente, caso contrário, o bloco except é acionado e a mensagem de erro é exibida.

try: #Inicio da leitura de dados solicitando os numeros
    numero1 = int(input("Digite o primeiro número: "))
    if numero1 <=0: # verificando se o número é maior que zero
        print('O numero digitado não é válido')
except ValueError: #Se digitar algo que não seja numero retorna a msg de erro do programa
    print("O valor digitado não é um número válido.")
try:
    numero2 = int(input('Digite o segundo numero '))
    if numero2 <=0:
        print('O numero digitado não é válido')
except ValueError:
    print("O valor digitado não é um número válido.")
try:
    numero3 = int(input('Digite o terceiro número'))
    if numero3 <=0:
        print('Ovalor digitado não é válido ')
except ValueError:
    print('O numero digitado não é válido')
try:
    numero4 = int(input('Digite o quarto número'))
    if numero4 <=0:
        print('O numero digitado não é válido')
except ValueError:
    print('O numero digitado não é válido')
try:
    numero5 = int(input('Digite o quinto número '))
    if numero5 <=0:
        print('Digite um número valdio')
except ValueError:
    print('O número digitado não é válido ')

if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5: 
    print('Primeiro número foi o número', numero1, 'ele é o maior')
elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
    print('Segundo número foi o número', numero2, 'ele é o maior')
elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
    print('Terceiro número foi o número', numero3, 'ele é o maior')
elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
    print('Quarto número foi o número', numero4, 'ele é o maior')
elif numero5 > numero1 and numero5 > numero2 and numero5 > numero3 and numero5 > numero4:
    print('Quinto número foi o número', numero5, 'ele é o maior')
else:
    print('Digite um numero válido')

