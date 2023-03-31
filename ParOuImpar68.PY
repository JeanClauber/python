from random import randint
print('-=' * 12)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=' * 12)

cont = 0

while True:
    jogador = int(input('Diga um numero: '))
    escolhaJogador = str(input('Par ou Impar? [P/I] ')).strip().upper()
    computador = randint(1, 10)
    print(f'Numero escolhido pelo PC foi {computador}')
    soma = computador + jogador
    
    if escolhaJogador == 'P' and soma % 2 == 0:
        print('Vitoria')
        cont += 1
        print('Vamos de novo!')
    elif escolhaJogador == 'I' and soma % 2 == 1:
        print('Vitoria')
        cont += 1
        print('Vamos de novo!')
    else:
        print(f'Você escolheu {escolhaJogador} o resultado deu {soma}')
        print(f'Eu venci e você ganhou {cont} vezes')
        break