from randon import choice

print('===== --- SORTEIO --- =====')

name = input('Digite o nome do primeiro aluno: ')
name2 = input('Digite o nome do segundo aluno: ')
name3 = input('Digite o nome do segundo aluno: ')
name4 = input('Digite o nome do segundo aluno: ')

lista = [name, name2, name3, name4]

escolhido = choice(lista)

print('O aluno escolhido foi: {}'.format(escolhido))