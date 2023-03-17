from math import radians, sin, cos, tan

ang = float(input('Digite um angulo: '))
seno = sin(radians(ang))
print('O angulo de {} tem o SENO de {:.2f}'.format(ang,seno))
cosseno = cos(radians(ang))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(ang,cosseno))
tangente = tan(radians(ang))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(ang,tangente))