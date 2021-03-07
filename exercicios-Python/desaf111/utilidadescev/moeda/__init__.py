def metade(preço=0, formato=False):
    met = preço / 2
    return met if formato is False else moeda(met)


def dobro(preço=0, formato=False):
    dob = preço * 2
    return dob if formato is False else moeda(dob)


def aumentar(preço=0, taxa=0, formato=False):
    aum = preço + ((preço * taxa) / 100)
    return aum if not formato else moeda(aum)

def diminuir(preço=0, taxa=0, formato=False):
    dim = preço - ((preço * taxa) / 100)
    return dim if not formato else moeda(dim)

def moeda(preço=0, moeda='R$', formato=False):
    return '{}{:.2f}'.format(moeda, preço).replace('.', ',')


def resumo(preço=0, taxaa=10, taxar=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print('Preço analizado: \t{}'.format(moeda(preço)))
    print('Dobro do preço: \t{}'.format(dobro(preço, True)))
    print('Metade do preço: \t{}'.format(metade(preço, True)))
    print('Com {}% de aumento: {}'.format(taxaa, aumentar(preço, taxaa, True)))
    print('Com {}% de redução: \t{}'.format(taxar, diminuir(preço, taxar, True)))