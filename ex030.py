"""Crie um programa que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR"""

numero = int(input('Digite um número qualquer...'))
resultado = numero % 2
if resultado == 0:
    print('O número é PAR')
else:
    print('O número é IMPAR')
