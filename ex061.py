"""Refaça o DESAFIO051, lendo o primeiro termo e a razao de uma PA, mostrando os 10 primeiros termos da progressao
usando a estrutura while"""

print('GERADOR DE PA')
print('-=-'* 10)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razao da PA: '))
termo = primeiro
cont = 1
while cont <=10:
    print('{} > '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')