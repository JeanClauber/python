while True:

    print('Selecione a operação desehada: ')
    print('1 - Soma')
    print('2 - Subtação')
    print('3 - Multiplicação')
    print('4 - Divisão')
    print('5 - Sair')

    escolha = input('Digite sua escolha: 1/2/3/4/5/ ')

    if escolha == '5':
        print('Saindo')
        break

    num1 = float(input('Digite o primeiro numero: '))
    num2 = float(input('Digite o segundo numero: '))

    if escolha == '1':
        resultado = num1 + num2
        print('O resultado da soma é: {}'.format(resultado))
    elif escolha == '2':
        resultado = num1 - num2
        print('O resultado da subtração é: {}'.format(resultado))
    elif escolha == '3':
        resultado = num1 * num2
        print('O resultado da multiplicação é: {}'.format(resultado))
    elif escolha == '4':
        if num2 == 0:
            print('Não é possivel dividir por zero!')
        else:
            resultado = num1 / num2
            print('O resultado da divisão é: '.format(resultado))
    else:
        print('Opção invalida. Tente novamente.')