def metade(me=0, formato=False):
    met = me / 2
    return met if formato is False else moeda(met)


def dobro(do=0, formato=False):
    dob = do * 2
    return dob if formato is False else moeda(dob)


def aumentar(au=0, taxa=0, formato=False):
    aum = au + ((au * taxa) / 100)
    return aum if not formato else moeda(aum)

def diminuir(di=0, taxa=0, formato=False):
    dim = di - ((di * taxa) / 100)
    return dim if not formato else moeda(dim)

def moeda(preço=0, moeda='R$', formato=False):
    return '{}{:.2f}'.format(moeda, preço).replace('.', ',')