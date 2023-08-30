import random

escolha = tamanho = 0

print('Bem vindo ao criador de senhas!')
 
while True:
    user_input = input("Digite um número entre 6, 8, 10 ou 12: ")
    
    if user_input in ["6", "8", "10", "12"]:
        tamanho = int(user_input)
        break 
    else:
        print("Numero incorreto, por favor apenas umas das opções.")

dificuldade = int(input('''Gostaria de uma senha 
    [1]fácil = apenas numeros 
    [2]media = numeros e letras
    [3]dificil = numeros, letras e simbolos
    [4]megahardoverpowersenhafoderosa \n'''))

if dificuldade == 1:
    numeros = "0123456789"
    unir = f"{numeros}{numeros}"
    longitude = tamanho
    extençao = random.sample(unir, longitude)
    senha = "".join(extençao)
    print(f'Sua senha é: {senha}. Não compartilhe com ninguem!')

elif dificuldade == 2:
    numeros = "0123456789"
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    unir = f"{numeros}{letras}"
    longitude = tamanho
    extençao = random.sample(unir, longitude)
    senha = "".join(extençao)
    print(f'Sua senha é: {senha}. Não compartilhe com ninguem!')

elif dificuldade == 3: 
    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numeros = "0123456789"
    simbolos = ".$%#@&!*+="

    unir = f"{letras}{numeros}{simbolos}"
    longitude = tamanho
    extençao = random.sample(unir, longitude)
    senha = "".join(extençao)

    print(f'Sua senha é: {senha}. Não compartilhe com ninguem!')

elif dificuldade == 4: 
    import random
    import time
    
    tentar = str(input('''Nessa dificuldade temos tres perguntas para saber se você merece uma senha MegaHard, você acredita que está pronto?
          [S]im
          [N]ão''')).lower()

    if tentar == 's':
        time.sleep(2)  
        print('Boa sorte!!!')
    

    def charada_1():
        print("O que é algo que sempre aumenta, nunca diminui, e é essencial para aprender e crescer?")
        resposta = input("Sua resposta: ").lower()
        return resposta == "conhecimento"

    def charada_2():
        print("Sou um animal que gosta de queijo e detesto gatos. Quem sou eu?")
        resposta = input("Sua resposta: ").lower()
        return resposta == "rato"

    def charada_3():
        print("Quanto mais você tira, mais cresce. O que é?")
        resposta = input("Sua resposta: ").lower()
        return resposta == "buraco"

    def main():
        charadas = [charada_1, charada_2, charada_3]
        charadas_certas = 0
        
        random.shuffle(charadas)
        
        for fase, charada in enumerate(charadas, start=1):
            print(f"Fase {fase}:")
            if charada():
                charadas_certas += 1
                if charadas_certas >= 3:
                    letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    numeros = "0123456789"
                    simbolos = ".$%#@&!*+="
                    l_acentos = "âáàèéìíòóúùÂÁÁÉÈÍÌÓÒÚÙ"
                    unir = f"{letras}{numeros}{simbolos}{l_acentos}"
                    longitude = tamanho
                    extençao = random.sample(unir, longitude)
                    senha = "".join(extençao)

                    print(f'Parabéns! Você acertou as 3 charadas. Sua senha MegaHard é: {senha}')
                    break
            else:
                print("Resposta incorreta! Você não merece essa senha.")
                break

    if __name__ == "__main__":
        main()
