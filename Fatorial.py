while True:
    fatorial = 1
    n = int(input('Digite um numero: '))
    for i in range(1, n+1):
        fatorial *= i
    print(fatorial)