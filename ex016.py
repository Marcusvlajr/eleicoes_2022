'''crie um programa que leia um número real qualquer pelo teclado e mostre na tela sua porcao inteira.
#ex. Digite um número: 6.127
#o numero 6.127 tem a parte inteira 6.
#from math import trunc or import math'''

'''or 
print('O valor digitado foi {} e sua porcao inteira é{}'.format(num, int(num)))'''
 import math
 num = float(input('Digite um numero: '))
 print('O valor digitado foi {} e sua porcao inteira é {}.'.format(num, math.trunc(num)))


"""import math
num = float(input('Digite um numero: '))
print('O valor digitado foi {} e sua porcao inteira é {}'.format(num, math.trunc(num)))"""
