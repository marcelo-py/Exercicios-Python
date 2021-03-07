jogadores = dict()
jogos = []
jogadores['nome'] = str(input('Nome: '))
total = int(input('Quantos jogos {} jogou? '.format(jogadores['nome'])))
for c in range(0, total):
    jogos.append(int(input('Quantos gols no jogo {} '.format(c+1))))
jogadores['gols'] = jogos[:]
jogadores['total'] = sum(jogos)
print(jogadores)
print('=' * 30)
for c, v in jogadores.items():
    print('{} tem o campo {} '.format(c, v))
print('=' * 30)
print('O jogador {} fez {} gols'.format(jogadores['nome'], jogadores['total'] ))
for c in range(0, len(jogos)):
    print('No {}º jogo fez {} gols'.format(c+1, jogos[c]))
print('Um total de {} gols'.format(sum(jogos)))