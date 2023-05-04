from time import sleep

n = int(input('Digite um numero: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(n, f+1, p):
    sleep(0.5)
    print(c)
print('FIM')