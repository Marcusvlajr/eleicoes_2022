"""Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas"""

distancia = float(input('Qual a distancia da sua viagem? '))
print('você está prestes a comecar uma viagem de {}km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))

