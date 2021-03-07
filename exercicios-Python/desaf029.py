import time
from emoji import emojize
velocidade = float(input('Qual a velocidade: '))
print('\033[32mAGUARDE...')
time.sleep(2)
if velocidade <=80:
    print('A velocidade ta no valor permitido')
else:
    preço = (velocidade-80)*7
    print(emojize('\033[1;7;34mMultado! vc excedeu a velocidade permitida de 80KM/h, você deve pagar a multa de :memo: {}R$\033[m'.format(preço)))
