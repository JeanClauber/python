while True:
    sexo = str(input('Digite F ou M: ')).upper()
    if sexo == 'M':
        print('Sexo Masculino')
        break
    elif sexo == 'F':
        print('Sex Feminino')
        break
    else:
        print('Por favor, escolha uma das opções.')
print('Obrigado por responder. :)')