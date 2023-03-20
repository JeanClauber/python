import random, time

jokenpo = ['pedra', 'papel', 'tesoura']


escolha_maquina = random.choice(jokenpo)
name = str(input('Digite seu nome: '))
time.sleep(1)
while True: 
    print('Olá {}! Bem vindo ao Jokenpo.'.format(name))
    print('Escolha: Pedra, Papel ou Tesoura')
    player = str(input('Digite sua escolha: ')).lower()

    time.sleep(0.5)
    print('JO')
    time.sleep(0.5)
    print('KEN')
    time.sleep(0.5)
    print('PO!!!')
    time.sleep(0.5)

    if player == 'pedra' or player == 'tesoura' or player == 'pedra':
        if player == 'pedra' and escolha_maquina == 'tesoura' or player == 'papel' and escolha_maquina == 'pedra' or player == 'tesoura' and escolha_maquina == 'papel':
            print('{} vence de {}, vitoria {}'.format(player, escolha_maquina, name))
            print(escolha_maquina)

        elif player == 'pedra' and escolha_maquina == 'pedra' or player == 'papel' and escolha_maquina == 'papel' or player == 'tesoura' and escolha_maquina == 'tesoura':
            print('Empate! O computador escolheu {} também'.format(escolha_maquina))

        else:
            print('Voce perdeu {} vence de {}, vitoria do computador'.format(escolha_maquina, player))
        break
    
    else:
        print('Opção invalida! Escolha uma das opções \n')
