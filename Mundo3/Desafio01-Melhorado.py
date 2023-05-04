from time import sleep
cont = 0
numeros = ('zero', 'um','dois','tres', 'quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte')


num = int(input('Digite um numero entre 0 e 20: '))
cont += 1

while num < 0 or num > 20:
    if cont <= 2:
        num = int(input('Numero inválido, digite um numero entre 0 e 20: '))
        cont += 1
    elif cont <= 3:
        print('Ultima chance...')
        sleep(1)
        num = int(input('Digite um numero entre 0 e 20: '))
        cont += 1
    elif cont >= 4:
        print('Tu é burro, é?')
        continuar = str(input('Eu vou encerrar o programa, quer tentar novamente? [S/N]')).lower()
        cont +=1
        if continuar == 's':
            print('Agora eu não quero mais! volte mais tarde')
            break
        else:
            print('Ainda bem porque eu não tinha mais paciente.')
            break

if cont > 3:
    print('Programa encerrado.')
else: 
    print(f'Você digitou o numero: {numeros[num].capitalize()}')