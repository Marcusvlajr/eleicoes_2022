""" Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa,
o salário do comprador e em quantos anos ele vai pagar,
AS prestação mensal nao pode exceder 30% do salário ou então o empréstimo será negado."""

#casa = float(input('Valor da casa: R$ '))
#salário = float(input('Salário do comprador: '))
#anos = int(input('Quantos anos de financiamento? '))
#prestação = casa / (anos * 12)
#mínimo = salário * 30 / 100
#print('Para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
#print('A prestação será de R${:.2f}'.format(prestação))
#if prestação <= mínimo:
# print('Empréstimo CONCEDIDO')
#else:
# print('Empréstimo NEGADO!')

casa = float(input('Valor da casa: RS: '))
salario = float(input('Qual seu salário: R$ '))
anos = int(input('Quantos anos voce quer pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30/ 100
print(f'Para pagar uma casa de {casa} em {anos}')
print(f'A prestacao da casa será de RS {prestacao}')
if prestacao <= minimo:
 print('APROVADO')
else:
 print('Emprestimo negado')

