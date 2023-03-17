sal = float(input('Qual o salario do funcionaro: '))

n_sal = sal + (sal * 0.15)

print('Um funcionario que ganhava R${:.2f}, com o aumento de 15% de aumento, passa a receber R${:.2f}'.format(sal,n_sal))