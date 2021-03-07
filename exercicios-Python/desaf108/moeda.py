def metade(me=0):
    met = me / 2
    return met


def dobro(do=0):
    dob = do * 2
    return dob


def aumentar(au=0, taxa=0):
    aum = au + ((au * taxa) / 100)
    return aum

def diminuir(di=0, taxa=0):
    dim = di - ((di * taxa) / 100)
    return dim

def moeda(preço=0, moeda='R$'):
    return '{}{:.2f}'.format(moeda, preço).replace('.', ',')