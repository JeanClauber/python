num1 = int(input('Digite um numero: '))

if num1 == 0 or num1 > 10:
    print('Numero invalido! Apenas numeros de 1 a 10')
else:
    for i in range(1, 11):
        print('{} x {} = {}'.format(num1,i, num1*i,))
        i += 1
print('Ai está a sua tabuada')