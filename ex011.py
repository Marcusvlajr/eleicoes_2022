#faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-lá,
 #cada litro de tinta pinta uma area de 2m ao quadrado. m m²

#larg = float(input('Largura da parede: '))
#alt = float(input('Altura da parede: '))
#area = larg * alt
#print('A parede tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
#tinta = area / 2
#print('Para pintar essa parede voce precisará de {}l de tinta'.format(tinta))

larg = float(input('Largura da parece: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('A parede tem a dimensao de {} x {} e sua area é de {}m²'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede voce precisará de {}l de tinta.'.format(tinta))


