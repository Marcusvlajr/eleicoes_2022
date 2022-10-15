#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salario com um aumento de 15%

salario = float(input('Valor do salário: R$'))
novo = salario + (salario * 15/100)
print('O salário R${:.2f} com 15% de aumento será R${:.2f}'.format(salario, novo))

ᵒc
