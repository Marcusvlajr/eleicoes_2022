"""A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria, de acordo com a idade:
-até 9 anos: mirim
-até 14 anos: infantil
-até 19 anos: junior
-até 25 anos: senior
-acima: master"""

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Categoria: MIRIN')
elif idade > 9 and idade <= 14:
    print('Categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('Categoria: JUNIOR')
elif idade > 19 and idade <= 25:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')
