n1 = float(input('Digite a nota da primeira prova: '))
n2 = float(input('Digite a nota da segunda prova: '))
n3 = float(input('Digite a nota da terceira prova: '))
nf = (n1 + n2 + n3) / 3
if nf >= 7:
    print('A nota foi {} aprovada'.format(nf))
elif nf <= 5:
    print('A nota foi {} reprovada'.format(nf))
