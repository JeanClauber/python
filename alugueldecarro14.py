days = float(input('Quantos dias alugados? '))
km = float(input('Quantos km foram rodados? '))

total = (days * 60) + (km * 0.15)

print('Total a pagar R${:.2f}'.format(total))