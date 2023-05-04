from datetime import date

ano_atual = date.today().year
MAIOR = 0
MENOR = 0

for i in range (1,8):
    ano_nasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(i)))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        MAIOR += 1
    else:
        MENOR += 1
print("""Temos {} maiores de idade 
e {} menores de idade""".format(MAIOR, MENOR))