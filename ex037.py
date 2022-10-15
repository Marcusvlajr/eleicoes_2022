"""Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para Binário
-2 para octal
-3 para hexadecimal"""

#num = int(input('Digite um número inteiro: '))
#print("""Escolha uma das bases para conversão:
#[1] converter para biário
#[2] converter para octal
#[3] converter para hexadecimal""")
#opção = int(input('Sua opção: '))
#if opção == 1:
 #   print('{} convertido pra binário é igual a {}'.format(num, bin(num)[2:]))
#elif opção == 2:
# print('{} convertido para octal é igual a {} '.format(num, oct(num)[2:]))
#elif opção == 3:
# print('{} convertido para hexadecimal é igual a {}'.format(num , hex(num)[2:]))
#else:
#    print('Opção INVALIDA')


num = int(input('Digite um numero inteiro: '))
print(""" Escolha uma das bases para conversão 
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal""")
opcao = int(input('Sua Opção: '))
if opcao == 1:
    print(f'{num} convertido a binário é {bin(num)[2]}')
elif opcao == 2:
    print(f'{num} convertido para octal e {oct(num)[2]}')
elif opcao == 3:
    print(f'{num} convertido para hexadecimal é {hex(num)[2]}')
else:
    print('Opção INVALIDA')
print('='*30)
print('Muito obrigado')





