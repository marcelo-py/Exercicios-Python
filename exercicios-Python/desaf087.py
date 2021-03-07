matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input('Digite um valor na posição [{}, {}]'.format(l, c)))
soma = somac =  0
print('\033[1;32mSua matriz\033[m')
for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        print('[{:^4}]'.format(matriz[l][c]),end='')
    print()
print('A soma entre todos os números pares digitado nela é: {}'.format(soma))
somac = somac + matriz[0][2] + matriz[1][2] + matriz[2][2]
print('A soma entre todos os números da 3ª coluna é {}'.format(somac))
print('O maior número da segunda linha é {}'.format(max(matriz[1])))
