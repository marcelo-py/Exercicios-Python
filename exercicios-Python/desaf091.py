from random import randint
from time import sleep
from operator import itemgetter
jogo = {'Jogador1': randint(1, 6),
        'Jogador2': randint(1, 6),
        'Jogador3': randint(1, 6),
        'Jogador4': randint(1, 6)}
print('Numeros sorteados')
for c, v in jogo.items():
    print('{} tirou {} no dado'.format(c, v))
    sleep(0.7)
print('====Ranking====')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for r, v in enumerate(ranking):
    print('{}º lugar: {} com {} pontos'.format(r+1, v[0], v[1]))
    sleep(0.7)