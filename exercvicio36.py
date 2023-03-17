import datetime

print('Verificar emmprestimo')

hour = datetime.datetime.now().hour
if hour > 12:
    print('Boa tarde!')
else:
    print('Bom dia!')
    
name = str(input('Para começar, digite seu nome: '))
house = float(input('Olá {}, qual o valor da casa que você deseja financiar? '.format(name)))
wage = float(input('Qual o seu rendimento mensal? '))
years = float(input('Em quantos anos? '))
mounths = years * 12
fees = 0.08 / 12
percentage = wage * 0.30

if mounths <= 361:
    per_mounth = (house / mounths)
    if per_mounth >= percentage:
        print('O valor da parcela fica {:.2f} está acima dos 30% liberado, credito não permitido'.format(per_mounth))
    else:
        print('Parabéns {}, seu credito será liberado o valor das parcelas serão de {:.2f} por {} meses.'.format(name, per_mounth, mounths))

else:
    per_mounth = (house * fees) / (1 - (1 + fees)**(-mounths))
    if per_mounth >= percentage:
        print('O valor da parcela fica {:.2f} está acima dos 30% liberado, credito não permitido'.format(per_mounth))
    else:
        print('Parabéns {}, seu credito será liberado o valor das parcelas serão de {:.2f} por {} meses.'.format(name, per_mounth, mounths))
