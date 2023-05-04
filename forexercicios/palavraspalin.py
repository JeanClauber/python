frase = str(input('Digite a palavra ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)

if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')
#print('Voce digitou a frase: {}'.format(frase))
