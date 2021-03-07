            # 0(par)    1(ímpar)_
print('{:^40}'.format('LISTA DE ITENS'))
listagem = ('lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,  #OBS a posição do produto ta sempre na posição par conferindo através do range
            'Estojo', 25,
            'Corretivo', 5,
            'Apagador', 9,
            'Caneta', 50)
for posi in range(0, len(listagem)):    #posição de 0 ao fim da lista, no caso os itens estão na posição 0 que é par e vou pedir para mostar eles
    if posi % 2 == 0:
        print('{:.<30}'.format(listagem[posi]),end='')
    else:       # se n for par é preço
        print('R${:>8.2f}'.format(listagem[posi]))
