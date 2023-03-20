from time import sleep

valor = float(input('Digite o valor do produto: '))
print('Qual será a forma de pagamento: ')

sleep(1)
print('1 - Dinheiro ou pix 10% de desconto')
sleep(1)
print('2 - a vista no cartão 5% de desconto')
sleep(1)
print('3 - Credito em até 2x preço normal')
sleep(1)
print('4 - 3x ou mais no cartão juros de 20%')

while True:
    escolha = int(input('Escolha 1 das opções: '))

    if escolha == 1:
        valor_desconto = valor - (valor * 0.10)
        print('Forma de pagamento será em dinheiro/pix, desconto de 10%')
        print('O valor fica R${:.2f}'.format(valor_desconto))

    elif escolha == 2:
        valor_desconto = valor - (valor * 0.05)
        print('Forma de pagamento escolhida cartão a vista 5% de dessconto')
        print('O valor fica R${:.2f}'.format(valor_desconto))

    elif escolha == 3:
        valor_juros = valor / 2
        print('Forma de pagamento escolhida credito no cartão em 2x.')
        print('O valor fica R${:.2f}'.format(valor_juros))
        print('O total é R${:.2f}'.format(valor))

    elif escolha == 4:
        print('Forma de pagamento credito em até 10x')
        print('Acima de 10x o juros fica 1% a mais por parcela adicional')
        sleep(1)
        vezes = int(input('Quantas parcelas : '))
        if vezes <= 10:
            valor_juros = valor + (valor * 0.20)
            parcelas = valor_juros / vezes
            sleep(1)
            print('O valor total fica R${:.2f}'.format(valor_juros))
            sleep(1)
            print('Parcelas no valor de R${:.2f}'.format(parcelas))
        else:
                adicional =  0.01 * (vezes - 10)
                valor_juros = valor + (valor *(0.20 + adicional))
                parcelas = valor_juros / vezes
                sleep(1)
                print('O valor total fica R${:.2f}'.format(valor_juros))
                sleep(1)
                print('Parcelas no valor de R${:.2f}'.format(parcelas))
        break
    else:
        print('Opção inválida!')
        print('Escolha uma das opções abaixo:')
        sleep(2)
        print('1 - Dinheiro ou pix 10% de desconto')
        print('2 - a vista no cartão 5% de desconto')
        print('3 - Credito em até 2x preço normal')
        print('4 - 3x ou mais no cartão juros de 20%')