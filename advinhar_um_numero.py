from random import choice
adv = int(input('Tente advinhar em qual número estou pensando! de 1 a 5: '))
lista = [1, 2, 3, 4, 5]
esc = choice(lista)
if adv == esc:
    print('Você acertou! Eu estava pensando no número {}'.format(esc))
else:
    print('Que pena, você errou! Eu estava pensando no numero {}'.format(esc))