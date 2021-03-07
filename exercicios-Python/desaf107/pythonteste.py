from desaf107 import moeda
p = float(input('Digite um preço: R$'))
print('A metade de {} é {}'.format(p, moeda.metade(p)))
print('O dobro de {} é {}'.format(p, moeda.dobro(p)))
print('Se adcionarmos 10% fica {}'.format(moeda.aumentar(p, 10)))
print('Se tirarmos 13%  fica {}'.format(moeda.diminuir(p, 13)))