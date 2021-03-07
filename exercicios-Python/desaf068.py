from random import randint
print('JOGO DO ÍMPAR OU PAR COM A MÁQUINA')
cont = 0
while True:
    pc = randint(0,11)
    print('='*25)
    pp = ' '
    while pp not in'PpIi':
        pp = str(input('Você escolhe PAR ou ÍMPAR? [P/I]: ')).strip().lower()
    jogador = int(input('Qual numero você escolhe?'))
    soma = pc + jogador
    if pp == 'p':
        if soma % 2 == 0:
            print('Computador: ÍMPAR {}\nJogador: PAR {}\nResultado=> {} (PAR)'.format(pc, jogador, soma))
            print('Joador Ganhou!!!')
            cont += 1
    if pp == 'p':
        if soma % 2 == 1:
            ip = 'ÍMPAR'
            pj = 'PAR'
            break
    if pp == 'i':
        if soma % 2 == 1:
            cont += 1
            print('Computador: PAR {}\nJogador: ÍMPAR {}\nResultado=> {} (ÍMPAR)'.format(pc, jogador,soma))
            print('Jogador Ganhou!!!')
    if pp == 'i':
        if soma % 2 == 0:
            ip = 'PAR'
            pj = 'ÍMPAR'
            break
print('Computador: {} {}\nJogador: {} {}\nResultado=> {}'.format(ip, pc, pj, jogador,soma))
print('Jogador PERDEU com {} vitorias '.format(cont))
