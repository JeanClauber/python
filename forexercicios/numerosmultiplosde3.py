

res = 0
cont = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        cont += 1
        res += c
        print(c)
print('O resultado de todos numeros é: {}'.format(res))
print('Existem {} valores solicitados'.format(cont))