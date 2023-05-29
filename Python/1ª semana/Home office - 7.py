# Faça um programa que capture uma frase e conte o número de caracteres de uma frase, não levando em consideração
# os espaços. Mostrar a frase e a quantidade encontrada

frase = input('Digite uma frase: ')

# Remove os espaços em branco da frase
frase_sem_espacos = frase.replace(' ', '')

# Conta o número de caracteres da frase sem espaços em branco
num_caracteres = len(frase_sem_espacos)

# Imprime a frase e o número de caracteres
print(f'Frase: {frase}')
print(f'Número de caracteres (sem espaços em branco):  {num_caracteres}')

# O programa solicita ao usuário para digitar uma frase e armazena essa frase na variável frase. Em seguida,
# ele utiliza o método replace() para remover todos os espaços em branco da frase e armazena a nova string na
# variável frase_sem_espacos. O programa conta o número de caracteres da frase sem espaços em branco utilizando a
# função len() e armazena o resultado na variável num_caracteres. Finalmente, o programa imprime a frase digitada
# pelo usuário e o número de caracteres contados.
