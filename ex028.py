"""Escreva um programa que faça o computador "pensar" em um númeri inteiro
entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu."""
import time
from random import randint
computatador = randint(0, 5)   #FAZ O COMPUTADOR PENSAR
print('-=-'* 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ') #Jogador tenta adivinhar.
print('-=-' * 20)
jogador = int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)
if computatador == jogador:
    print('PARABÉNS! Você conseguiu me vencer.')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(computatador, jogador))


