def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro digite um número válido\033[m')
        if ok:
            break
    return valor

#main program
n = leiaInt('Digite um numero')
print('Você digitou o numero {}'.format(n))
