frase = input('Digite uma frase: ')

num_caracteres = 0

for c in frase:  # c variavel caracter
    if c.isalpha():  # isalpha() método, classe str que retorna True se todos os caracteres são letras maiúsculas ou mn
        num_caracteres + 1

print(f'Frase: {frase}')
print(f'Número de caracteres (sem espaços em branco): {num_caracteres}')
