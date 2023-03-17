salario = float(input('Digite o seu salario: '))

if salario >= 1251:
    A_sal = salario + (salario * 0.10)
    print('Seu salario com aumento de 10% ficará: R${:.2f}'.format(A_sal))
else:
    A_sal = salario + (salario * 0.15)
    print('Seu salario com aumento de 15% ficará: R${:.2f}'.format(A_sal))
