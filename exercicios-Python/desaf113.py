def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um número inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('O usuario optou por sair')
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mErro! Digite um número real válido\033[m')
            continue
        else:
            return n


ni = leiaInt('Digite um numero inteiro ')
nf = leiaFloat('Digite um número real agora')
print('Usuario digitou o numero inteiro {} e o real {} '.format(ni, nf))