# Crie um programa que tenha uma tupla com varias palavras (nao
# usar acentos).
# Depois disso, voce deve mostrar, para cada palavra, quais sao as suas
# vogais

# Definindo a tupla com as palavras
palavras = ('python', 'programacao', 'computador', 'linguagem', 'openai')

# Função para encontrar as vogais em uma palavra
def encontrar_vogais(palavra):
    vogais = 'aeiou'
    vogais_encontradas = []
    for letra in palavra:
        if letra.lower() in vogais:
            vogais_encontradas.append(letra)
    return vogais_encontradas

# Exibindo as vogais de cada palavra na tupla
for palavra in palavras:
    vogais = encontrar_vogais(palavra)
    print(f'Palavra: {palavra} | Vogais: {vogais}')
