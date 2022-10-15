#Faça um algoritmo que leia o preço do produto e mostre seu novo preço com desconto de 5%

"""preco = float(input('Qual é o preço do produto? R$: '))
novo = preco - (preco * 5/100)
print('O produto que custava R${:.2f}, com o desconto de 5% vai custar R${:.2f} '.format(preco, novo))"""

preco = float(input('Qual é o preço do produto? '))
novo = preco - (preco * 5/100)
print('O produto que custava {}, com o desconto de {}%, agora vai custar {}.'.format(preco, novo))
