"""faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
e o menos peso lidos."""

maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('peso da {} pessoa '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {:.2f}KG'.format(maior))
print('O menor peso lido foi de {:.2f}kg'.format(menor))



