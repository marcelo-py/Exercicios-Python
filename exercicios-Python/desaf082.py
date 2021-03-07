lista = []
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    sn =  str(input('Deseja continuar? [S/N] '))
    while not sn in 'SsNn':
        sn = str(input('Deseja continuar? [S/N] '))
    if sn in 'Nn':
        break
print('A lista compreta é {}'.format(lista))
for p in lista:
    if p % 2 == 0:
        par.append(p)
for i in lista:
    if i % 2 == 1:
        impar.append(i)
print('Os números pares foram {}'.format(par))
print('Os números Ímpares foram {}'.format(impar))