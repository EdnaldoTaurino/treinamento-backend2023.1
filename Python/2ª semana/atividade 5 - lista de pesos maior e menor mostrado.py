# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

lista_peso = []

for i in range(5):
    peso = float(input('Digite seu peso: '))
    lista_peso.append(peso)
    maior_peso = max(lista_peso)
    menor_peso = min(lista_peso)

print(f''' 
O menor peso foi: {menor_peso}
O maior peso foi {maior_peso}''''')


