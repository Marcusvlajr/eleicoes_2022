"""Faça um programa que calcule a soma entre todos os números ímpares que são
multiplos de tres e que se encontram no intervalo de 1 ate 500"""
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1 #opcao de iniciante
        soma += c #opcao mais usada
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

