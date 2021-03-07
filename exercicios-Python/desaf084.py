geral = list()
nomepeso = list()
maiorpeso = list()
while True:
    nomepeso.append(str(input('Nome: ')))
    nomepeso.append(int(input('Peso: ')))
    geral.append(nomepeso[:])
    nomepeso.clear()
    sn = str(input('Deseja continuar? [S/N] '))
    if sn in 'Nn':
        break
for c in geral:
    maiorpeso.append(c[1])
print('O maior peso foi {}Kg de '.format(max(maiorpeso)),end=' ')
for p in geral:
    if p[1] == max(maiorpeso):
        print(p[0],end=', ')
print('\nOs mais leves foram {}'.format(min(maiorpeso)),end=' ')
for p in geral:
    if p == min(maiorpeso):
        print(p[0])


