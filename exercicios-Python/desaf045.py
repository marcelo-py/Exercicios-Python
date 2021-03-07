import random
from emoji import emojize
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
print (emojize('''Suas opções:
[0] PEDRA :punch:
[1] PAPEL :hand:
[2] TESOURA :v:''',use_aliases=True))
escolha = int(input('Qual sua escolha? '))
computador = random.randint(0,2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*20)
print('O computador escolheu {}'.format(itens[computador]))
if escolha == 0:
    print('Você escolheu PEDRA')
    if computador == 1:
        print('Você perdeu')
    elif escolha == computador:
        print('EMPATE')
    elif computador == 2:
        print('Você ganhou!!!')
elif escolha == 1:
    print('Você escolheu PAPEL')
    if computador == 2:
        print('Você perdeu')
    elif escolha == computador:
        print('EMPATE')
    elif computador == 0 :
        print('Você ganhou!!!')
elif escolha == 2:
    print('Você escolheu TESOURA')
    if computador == 0:
        print('Você perdeu')
    elif escolha == computador:
        print('EMPATE')
    elif computador == 1 :
        print('Você ganhou!!!')
print('=-'*20)
