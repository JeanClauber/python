total = cont = barato =0
valores = []
while True:
    produto = str(input('Produto: '))
    valor = float(input('Preço: '))
    total += valor
    continuar = str(input('Quer cadastrar mais produtos? [S/N] ')).upper()
    valores.append(valor)
    barato = min(valores)
    if valor > 1000:
        cont += 1

    if continuar == 'N':
        break

print(f'O total de todos os produtos é: R${total}')
print(f'Na lista tem {cont} produtos que custam acima de R$ 1000.')
print(f'O produto mais barato custa R${barato}')

