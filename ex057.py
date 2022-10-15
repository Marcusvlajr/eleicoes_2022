"""Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitacao novamente ate ter um valor correto."""

sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'MFmf':
    sexo = str(input('Dados invalidos. Por favor, Informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))