cont = ('zero','um','dois','tres','quatro','cinco','seis',
        'sete','oito','nove','dez','onze','doze',
        'treze','quatorze','quinze','dezesseis','dezessete',
        'dezoito','dezenove','vinte')
while True:
    num = int(input('Digite um numero entre zero e vinte: '))
    if 0 <= num <= 20:
        break
    print('TENTE NOVAMENTE! ', end='')
print(f'Voce digitou {cont[num]}')
