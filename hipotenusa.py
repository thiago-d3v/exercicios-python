from math import sqrt, pow
co = float(input('Digite o comprimento do cateto oposto:'))
ca = float(input('Digite o comprimento do cateto adjascente:'))
h = sqrt(pow(co, 2) + (pow(ca, 2)))
print('Levando em consideracao o comprimento de {} para o cateto oposto e {} para o cateto adjascente.'.format(co, ca))
print('O comprimento da hipotenusa e {:.2f}'.format(h))