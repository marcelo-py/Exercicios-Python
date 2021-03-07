dadosd = dict()
jogadores = list()
gols = list()
while True:
    dadosd['nome'] = str(input('Nome: '))
    total = int(input('Quantas partidas {} jogou? '.format(dadosd['nome'])))
    for c in range(0, total):
        gols.append(int(input('Quantos gols no {}º jogo? '.format(c+1))))
        dadosd['gols'] = gols[:]
    gols.clear()
    jogadores.append(dadosd.copy())
    dadosd.clear()
    sn = str(input('Quer continuar? S/N '))
    while sn not in 'SsNn':
        sn = str(input('Quer continuar? S ou N'))
    if sn in 'Nn':
        break
print('Nº |   Nome   |    Gols    |  Total')
for i, p in enumerate(jogadores):
    print('{}    {}     {}   {}'.format(i, p['nome'], p['gols'], sum(p['gols'])))
print('=-'*30)
while True:
    num = int(input('Ler dados de qual jogador? (999 para sair) '))
    if num == 999:
        break
    if num >= len(jogadores):
        print('Erro!!! numero não está na lista')
    if num <= len(jogadores)-1:
        print('Levantamento do jogador {}'.format(jogadores[num]['nome']))
        for i, v in enumerate(jogadores[num]['gols']):
            print('=> No {}º jogo fez {} '.format(i+1, v))
