from random import randint
from time import sleep
from emoji import emojize
escolha = int(input('Digite um numero de 0 a 5 para jogar '))
pensando = randint(0,5)
print (emojize('PROCESSANDO... :anguished: ', use_aliases=True))
sleep(2)
if pensando == escolha:
    print(emojize(':hushed: Parabens vc conseguiu acertar', use_aliases=True))
else:
    print(emojize('Que pena pensei no {} e não no {} :stuck_out_tongue_closed_eyes:'.format (pensando, escolha), use_aliases=True))
