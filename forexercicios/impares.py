num = int(input('Digite um numero: '))
cont = 0
for i in range (1, num):
    if cont % 2 == 1:
        impar = cont
        print('{}'.format(impar))
    cont += 1
