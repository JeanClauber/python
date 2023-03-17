nome = str(input('Qual é o seu nome: '))
if nome == 'Jean':
    print('Que nome bonito!!!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jessia Juliana':
    print('Belo nome')
else: 
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}'.format(nome))