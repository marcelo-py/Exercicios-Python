from random import randint
from time import sleep
def sorteia(lista):
    print('Sorteado números')
    for c in range(0,5):
        n = randint(0, 10)
        lista.append(n)
        print('\033[1;34m{}'.format(n),end=' ')
        sleep(0.35)
    print('=> \033[7;1;33m{}\033[m \033[1;34mFIM!'.format(lista))
    soma = 0
    print('\033[1;32mOs números pares da lista foram...',end=' ')
    for v in lista:
        if v % 2 == 0:
            print('\033[7;1m{}\033[m'.format(v),end=' ')
            soma += v
    print('\033[7;1mTotal de {}\033[m'.format(soma))


#Programa principal
num = list()
sorteia(num)