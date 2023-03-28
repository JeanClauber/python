from random import randint
from time import sleep

cont = 0

while True:
    print('Pensando em um numero', end='')
    for i in range(1, 4):
        sleep(1)
        print('.', end='', flush=True)

    maquina = randint(1, 10)

    jogador = int(input('\nEscolha um nunero de 1 até 10: '))

    if maquina == jogador:
        break
    else: 
        print('Tente novamente')
        print('O numero era {}'.format(maquina))
        cont += 1
print('Parabéns! Você acertou o numero era {} e você precisou de {} tentativas.'.format(maquina, cont))
