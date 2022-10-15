num = []
pares = []
impar = []
while True:
    num.append(int(input('Digite um numero: ')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*30)
print(f'A lista comppleta é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista impar é {impar}')

