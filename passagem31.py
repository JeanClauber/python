distancia = float(input('Digite a distancia da sua viagem: '))

if distancia <= 200:
    total = distancia * 0.50
    print('Sua viagem tem menos de 200km, o valor que você vai pagar pé: R${:.2f}'.format(total))
else:
    total = distancia * 0.45
    print('Sua viagem tem mais de 200km, o valor a ser pago é: R${:.2f}'.format(total))