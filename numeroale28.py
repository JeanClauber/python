from random import randint
from time import sleep

number = randint(1, 5)
print('-=-' * 18)
print('Vou pensar em um numero entre 1 e 5, tente adinhar...')
print('-=-' * 18)
num1 = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
sleep(2)


if num1 == number:
    print('Parabens! O numero pensado era: {}'.format(number))
else: 
    print('Você errou! O numero que esu estava pensando era {}, e não {}'.format(number, num1))


