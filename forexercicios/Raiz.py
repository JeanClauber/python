from math import sqrt

for i in range(1, 1001):
    raiz = sqrt(i)
    i += 1
    if raiz % 2 == 1:
        print('a raiz quadrada de {} é, e {} é impar'.format(i, raiz))