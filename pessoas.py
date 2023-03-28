print('-=' * 10)
print('PESSOAS PARA ATENDER')
print('-=' * 10)
cont = 0
r = 'SIM'
while r == 'SIM':
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    cont += 1
    r = str(input('Gostaria de registrar mais alguem? [Sim/Nao]: ')).upper()

print('Você registrou {} pessoas'.format(cont))