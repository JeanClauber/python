from random import randint
sorteados = []

for c in range(0,5):
    sorteados.append(randint(1,10))
    
menor = min(sorteados)
maior = max(sorteados)

print(f'Os numeros sorteados foram:{sorteados}')
print(f'O menor numero sorteado foi: {menor}')
print(f'O maior numero sorteado foi: {maior}')