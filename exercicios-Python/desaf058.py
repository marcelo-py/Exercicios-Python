from random import randint
#computador = randint(1,10)
#print('''Acabei de pensar em um numerode 1 a 10.
#Você pode adivinhar qual foi?''')
#pessoa = 0
#tentativa = 0
#while pessoa != computador:
    #pessoa = int(input('Qual o seu palpite?'))
    #if pessoa != 0:
       # if pessoa < computador:
        #    print('Maior...',end='')
     #   if pessoa > computador:
       #     print('Menor...',end='')
    #    tentativa += 1
   # if pessoa != computador:
   #     print('Tente de novo')
#print('Parabens!!! Você ganhou com {} tentativas'.format(tentativa))


computador = randint(0,10)
print('Acabei de pensar entre um número de 0 a 10')
print('Será que você consegue adivinhar qual foi?')
acertou = False
tentativa = 0
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    tentativa += 1
    if jogador == computador:
        acertou = True
    elif jogador < computador:
        print('Mais...',end='')
    elif jogador > computador:
        print('Menos...',end='')
print('Acertou! com {} tentativas'.format(tentativa))
