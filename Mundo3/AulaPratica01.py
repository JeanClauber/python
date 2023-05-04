#Parenteses sao para tuplas, tuplas não podem ser modificadas são imutaveis

lanche = ('hamburguer','suco','pizza','pudim')
print(lanche) #mostra a tupla inteira
print(lanche[1]) #m mostra apenas o suco
print(lanche[2:]) #mostra da pizza em diante
print(lanche[:2]) # mostra do 0 até 02 que é a pizza
print(lanche[-1]) # mostra ao contrario

# Mostra a lista dos lanches
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('Comi pra caramba!')
print('\n')
# mesma funçãode cima, so que de uma forma mais simples, mas preferese usar a de cima.
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('\n')
#Mostra as posições dos lanches
for comida in enumerate(lanche):
    print(f'Eu vou comer {comida}')

#mostra a tupla em ordem alfabetica
print(sorted(lanche))
