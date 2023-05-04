a = (2, 5, 4)
b = (5, 8 ,1 ,2)
c = a + b
print(c)
print(sorted(c)) #deixa do menor ao maior ou ordem alfabetica
print(len(c)) #conta quantos elemento tem dentro
print(c.count(5)) #conta quantos numeros 5 tem dentro das tuplas que estão juntas. neste caso tem 2 numeros 5.
print(c.index(8)) #mostra a posição do numero 8 neste caso é a 4 posção.

print('\n')

pessoa = ('Jean', 29, 'M', 99.88)
del(pessoa) #apaga a tupla inteira
print(pessoa)