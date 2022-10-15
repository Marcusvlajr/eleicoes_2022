"""Escreva um programa que leia dois números inteiros e compare-os
mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Nao existe valor maior, os dois sao iguais"""

#n1 = int(input('Digite um valor: '))
#n2 = int(input('Digite outro valor '))
#if n1 > n2:
#    print('O primeiro valor é maior')
#elif n1 < n2:
#    print('O segundo valor é maior')
#else:
# print('Não existe valor maior, os dois são iguais')
#print('MUITO OBRIGADO')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('O primeiro valor é maior')
elif n1 < n2:
    print('O Segundo valor é maior: ')
else:
    print('Não existe valor maior, os dois são iguais')
print('='*30)
print('MUITO OBRIGADO')
