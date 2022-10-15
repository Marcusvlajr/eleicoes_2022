"""Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
e condicao de pagamento:
- a vista ( dinheiro / cheque, 10% de desconto)
- a vista ( cartao, 5% de desconto)
-em até 2x no cartao: preco normal
3x ou mais no cartao: 20% de juros"""

print('{:=^40}'.format(' LOJAS ALMEIDA  '))
preco = float(input('Preço das compras: R$: '))
print('''FORMAS DE PAGAMENTO:
[1] à vista dinheiro / cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x no cartão''')
opcao = int(input('Qual é a opção: '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = preco / 2
    print('Sua compra será parcelada wem 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/ 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(totparc, parcela))

print('Sua compra de R$:{:.2f}, vai custar R$:{:.2f} no final.'.format(preco, total ))
