res = 0
cont = 0

for c in range(1, 7):
    num = int(input('Digite o {}° valor: '.format(c)))
    if num % 2 == 0:
        res += num
        cont += 1
print('Você informou {} numeros e a soma dos numeros pares são: {}'.format(cont, res))