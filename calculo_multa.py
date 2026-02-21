dis = int(input('Digite a distancia da viagem Km:'))
if dis < 200:
    print('O preço para viagens de ate 200km é de R$0,50 por cada Km')
    print('Em uma viagem de {}km, o preço da passagem fica R${:.2f}'.format(dis, dis * 0.50))
else:
    print('O preço para viagens acima de 200km é de R$0,45 por cada Km')
    print('Em uma viagem de {}km, o preço da passagem fica R${:.2f}'.format(dis, dis * 0.45))
