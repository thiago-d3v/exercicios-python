prod = float(input('Quanto custa o produto? R$'))
desc = int(input('Digite a porcentagem do desconto:'))
val = prod - ((desc / 100) * prod)
print('o produto com um desconto de {}% custa {:.2f}'.format(desc, val))