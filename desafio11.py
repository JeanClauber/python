alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura: '))

area = larg * alt

print('Uma parede de {}x{} e a sua area é de {}m²'.format(alt,larg,area))

tinta = area / 2

print('Para pintar essa parede, você precisara de {}l de tinta.'.format(tinta))
