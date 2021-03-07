from desaf109 import moeda
p = float(input('Digite um preço: R$'))
print('A metade de {} é {}'.format(moeda.moeda(p), moeda.metade(p, True)))
print('O dobro de {} é {}'.format(moeda.moeda(p), moeda.dobro(p, True)))
print('Se adcionarmos 10% fica {}'.format(moeda.aumentar(p, 10, True)))
print('Se tirarmos 13%  fica {}'.format(moeda.diminuir(p, 13, True)))