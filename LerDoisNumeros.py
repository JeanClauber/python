from time import sleep

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite outro numero: '))

while True:


    print('''
    [1] Soma
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do Programa \n''')
    escolha = int(input('Escolha uma das opções a cima: '))

    if escolha == 1:
        res = n1 + n2
        print('A soma de {} + {} é {}'.format(n1,n2,res))
    elif escolha == 2:
        res = n1 * n2
        print('A multiplicação de {} x {} é igual {}'.format(n1,n2,res))
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n1 == n2:
            print('Os numeros são iguais.')
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif escolha == 4:
        print('Escolha novos numeros')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite outro numero: '))

    elif escolha == 0 or escolha >= 6:
        print('Opção invalida! Escolha uma das opções ou [5] para finalizar o programa')

    elif escolha == 5:
        print('Encerrando programa em ')
        for i in range(3, 0, -1):
            sleep(1)
            print('{}'.format(i), flush=True)
            i -= 1
        break
print('Programa encerrado!')