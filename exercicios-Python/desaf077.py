lista = ('Caderno', 'Caneta', 'Carro', 'Esteira', 'Computador', 'Gaiola', 'TPL', 'QWRT')
for p in lista:
    print('\nPara a palavra {} temos '.format(p.upper()),end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print('{}'.format(letra),end='')
