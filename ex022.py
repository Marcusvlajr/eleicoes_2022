"""'Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (Sem considerar espaços)
Quantas letras tem o primeiro nome:
"""

'''nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome... ')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))'''

nome = str(input('Digite seu nome:  ')).strip()
print('Seu nome completo tem {} letras'.format(len(nome)- nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

