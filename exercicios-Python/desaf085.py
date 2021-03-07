""""pares = list()
impares = list()
valores = list()
for v in range(1,8):
    valores.append(int(input('Digite o {}º numero'.format(v))))
for i in valores:
    if i % 2 == 1:
        impares.append(i)
    else:
        pares.append(i)
pares.sort()
impares.sort()
print('''Os números Pares são {}
Os Ímpares são {}'''.format(pares, impares))"""""

num = [[],[]]
for c in range(1, 8):
    numeros = int(input('Digite o {}º numero '.format(c)))
    if numeros % 2 == 1:
        num[0].append(numeros)
    else:
        num[1].append(numeros)
num[0].sort()
num[1].sort()
print('Os números Ímpares digitados foram \033[1;32m{}\033[m'.format(num[0]))
print('Os números Pares digitados foram \033[1;35m{}'.format(num[1]))
