"""Crie um programa que simule o funcionamento de um caixa eletronico.
No inicio, pergunte ao usuario qual será o valor a ser sacado (numero inteiro)
e o programa vai informar quantas cedulas de cada valor serao entregues.
OBS: Considere que o caixa possui cédulas de 50/20/10/1."""

print('-'* 30)
print('{:^30}'.format('BANCO KHS'))
print('-'* 30)
valor = int(input('Que valor você quer sacar? R$: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R$ {ced}')
        if  ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('-'*30)
print('Volte sempre ao BANCO KHS. Tenha um bom dia')


