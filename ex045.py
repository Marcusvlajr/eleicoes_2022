"""Crie um programa que faça o computador jogar jokenpô com você."""

from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(2)

print('-=' * 15)
print('Computador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}'.format(itens [jogador]))
print('=-' *15)

if computador == 0:
    if jogador == 0:
        print('EMPATE!')

    elif jogador == 1:
        print('PERDEU')


    elif jogador == 2:
        print('PERDEU')

    else:
        print('Opçao Inválida.')
elif computador == 1:
    if jogador == 0:
        print('GANHOU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('GANHOU')

    else:
        print('Opção Inválida.')

elif computador == 2:
    if jogador == 0:
        print('GANHOU')

    elif jogador == 1:
        print('PERDEU')

    elif jogador == 2:
        print('EMPATE')

    else:
        print('Opção Inválida.')






