n_itens = int(input('Quantos itens quer adicionar a sacola: '))
itens = ['']
for i in range(1, n_itens +1):
    itens = str(input('Digite o {}° item: '.format(i)))
    itens += itens
print(itens)