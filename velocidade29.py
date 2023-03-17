vel = int(input('Qual a velocidade do carro: '))

if vel >= 81:
    multa = 7 * (vel - 80)

    print('Você está acima da velocidade permitida de 80km')
    print('Você foi multado por cada km a cima da velocidade permitida e o valor ficou: R${}'.format(multa))

else:
    print('Sua velocidade está ok')