termo = int(input('Primeiro termo'))
razão =int(input('Razão da PA'))
r = termo
cont = 1
while cont <=10:
    print('{} > '.format(r),end=' ')
    r += razão
    cont += 1
print('FIM')