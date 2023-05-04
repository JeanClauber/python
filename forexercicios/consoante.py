while True:
    letra = input("Digite uma letra: ")
    if letra.lower() == 'sair':
        print('Você fechou o programa, verme')
        break
    if letra.lower() in 'aeiou':
        print(letra, "é uma vogal")
    else:
        print(letra, "é uma consoante")

