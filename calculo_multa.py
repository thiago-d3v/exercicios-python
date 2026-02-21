speed = int(input('O limite de velocidade dessa rodovia é 80Kmh\n Qual é a velocidade atual do seu carro? KMh: '))
if speed > 80:
    print('Você ultrapassou o limite de velocidade!')
    print('Será enviado uma multa no valor de R$7,00 por cada Km excedido ao limite de velocidade!')
    print('A multa ficara no valor de R${}.'.format((speed - 80) * 7))
else:
    print('Você está dentro do limite de velocidade da rodovia\nTenha uma boa viagem! ')
