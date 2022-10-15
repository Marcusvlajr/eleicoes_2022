"""Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC, e mostre seu status,
de acordo com a tabela abaixo:
-Abaixo de 18.5: abaixo do peso
-entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
-30 ate 40: obesidade
- acima de 40: Obesidade mórbida"""

peso = float(input('Qual o seu peso: (kg)'))
alt = float(input('Qual a sua altura: (m)'))
imc = peso / alt ** 2
print('o IMC do Feliphe é {:.1f}, e ele está com OBESIDADE MÓRBIDA'.format(imc))