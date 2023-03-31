from time import sleep

pessoas = homens = mulheres = 0

while True:
    sexo = str(input('[M/F]: ')).upper()
    idade = int(input('Idade: '))
    res = str(input('Quer continuar? [S/N]')).upper()
    
    if res == 'S':
        if idade > 18:
            pessoas += 1
        if sexo == 'M':
            homens += 1
            pessoas += 1
        if sexo == 'F':
            if idade < 20:
                pessoas += 1
                mulheres += 1
            else:
                pessoas += 1
    elif res == 'N':
        break

print('Fim do programa')
sleep(0.5)
print(f'Foram cadastradas {pessoas} pessoas')
sleep(0.5)
print(f'Existem {homens} homens cadastrados')
sleep(0.5)
print(f'Existem {mulheres} cadastradas menores de 20 anos.')