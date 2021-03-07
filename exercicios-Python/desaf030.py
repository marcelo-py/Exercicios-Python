import emoji
import playsound
from time import sleep
valor = int(input('Digite um valor '))
resultado = valor%2
if resultado == 1:
    print (emoji.emojize('O número {} é ímpar :point_up:'.format (valor), use_aliases=True))
else:
    print (emoji.emojize('O número {} é par :v:'.format(valor),use_aliases=True))
print('AGUARDE...')
sleep(3)
print (emoji.emojize('\033[7;34mTocando... Latch- Sam Smith :notes: :alien:\033[m',use_aliases=True))
playsound.playsound('desaf021.mp3')
