n1 = float(input('Digite o valor do primeiro lado: '))
n2 = float(input('Digite o valor do segundo lado: '))
n3 = float(input('Digite o valor do terceiro lado: '))

if (n1 + n2 > n3) and (n1 + n3 > n2) and (n1 + n3 > n2):
    print('Pode formar um trindulo')
else:
    print('Não pode formar um triangulo')