#   print('\033[1;30;45mOlá caralhomundo!\033[m')

nome = input('Digite seu nome: ')
cores = {'limpa':'\033[m','azul':'\033[34m','amarelo':'\033[33m','verde':'\033[32m'}

print('Seu nome é {} {} {}'.format(cores['verde'],nome,cores['limpa']))

