# Lê os três números do usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

# Verifica se os números são iguais ou diferentes
if numero1 == numero2 == numero3:
    print("Três números iguais!")
elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
    print("Dois números iguais!")
else:
    print("Três números diferentes!")
