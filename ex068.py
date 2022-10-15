"""Faça um programa que jogue PAR ou IMPAR com o computador. O jogo só será interrompido
quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou
no final do jogo"""

from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I]')).strip().upper()
    print(f'Voce jogou {jogador} e o computador {computador}. total de {total}', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('voce VENCEU.')
        else:
            print('Voce PERDEU.')
            break
    elif tipo  == 'I':
        if total % 2 == 1:
            print('VOCE VENCEU.')
            v += 1
        else:
            print('VOCE PERDEU.')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! Voce venceu {v} vezes.')