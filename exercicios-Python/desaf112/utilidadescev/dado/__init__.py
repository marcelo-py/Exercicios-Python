def leiaInt(msg):
    valido = False
    while not valido:
        mg = str(input(msg)).replace(',', '.')
        if mg.isalpha() or mg.strip() == '' :
            print('\033[1;31mErro! não posso ler "{}", digite um número valido\033[m'.format(mg))
        else:
            valido = True
            return float(mg)

def dinheiro(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mErro digite um número válido\033[m')
        if ok:
            break
    return valor