from time import sleep

num = int(input('Digite um numero: '))

for c in range (0, 11):
    sleep(0.5)
    print('{} x {} = {}'.format(num, c, c*num))
    c += + 1

print('Pronto! Essa é a tabuada do {}'.format(num))