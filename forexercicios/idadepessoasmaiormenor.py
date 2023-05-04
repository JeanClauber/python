print('-=' * 9)
print('Peso das pessoas')
print('-=' * 9)

maior = 0
menor = 0

for p in range(1, 5 + 1):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
