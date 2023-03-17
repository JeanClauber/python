import math

n1 = float(input('Digite o comprimento do cateto oposto: '))
n2 = float(input('Digite o cateto adjacente: '))

hipo = math.hypot(n1,n2)

print("A hipotenusa é {:.2f}".format(hipo))