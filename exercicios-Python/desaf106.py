c = ('\033[m',
     '\033[7;1;30m',
     '\033[7;1;31m',
     '\033[7;1;32m',
     '\033[7;1;33m'
     )


def ajuda(com):
    titulo('Acessando o Manual \'{}\''.format(com), 4)
    print(c[1], end='')
    help(com)
    print(c[0], end='')


def titulo(t, cor = 0):
    tam = len(t) + 4
    print(c[cor], end='')
    print('~'*tam)
    print('  {}'.format(t))
    print('~'*tam)
    print(c[0],end='')


#Programa Princiapl
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    comando = input(str('Função ou biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Obrigado, Volte sempre', 3)