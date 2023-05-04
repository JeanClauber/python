idadeTotal = 0
maioridadehomem = 0
nomevelho = 0
totmulher20 = 0

for i in range(1, 4+1):
    print('----- {}° PESSOA -----'.format(i))
    nome = str(input('Nome da pessoa: ')).strip()
    sexo = str(input('Sexo [M/F]')).strip()
    idade = int(input('Qual a idade: '))
    idadeTotal += idade
    if i == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


media = idadeTotal / 4

print('A idade média do grupo é {}'.format(media))
print('O homem mais velho tem {} e se chama {}'.format(maioridadehomem,nomevelho))
print('Ao todo são {} mulheres com menso de 20 anos.')