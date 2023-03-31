cont = n = 0

while True:
    print('-' * 35)
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n} x {cont} = {cont*n}')
print('Você Encerrou a tabuada.')
