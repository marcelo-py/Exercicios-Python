matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor na posição [{}, {}]'.format(l, c)))
cont = 0
for l in range(0, 3):
    for c in range(0, 3):
        print('[{:^5}]'.format(matriz[l][c]),end='')
    print()
