frase = input('Digite uma frase: ')
letra = input('Qual letra voce quer encontrar na frase? ')

res = frase.count(letra)

print('Existem {} letras {} na frase' .format(res,letra))