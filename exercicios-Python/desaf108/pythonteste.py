from desaf108 import moeda
p = float(input('Digite um preço: R$'))
print('A metade de {} é {}'.format(moeda.moeda(p), moeda.moeda(moeda.metade(p))))
print('O dobro de {} é {}'.format(moeda.moeda(p), moeda.moeda(moeda.dobro(p))))
print('Se adcionarmos 10% fica {}'.format(moeda.moeda(moeda.aumentar(p, 10))))
print('Se tirarmos 13%  fica {}'.format(moeda.moeda(moeda.diminuir(p, 13))))