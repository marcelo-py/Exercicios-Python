from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja '))
seno = sin(radians(angulo))
print('O seno de {}º é {:.2f}'.format (angulo, seno ))
cosseno = cos(radians(angulo))
print('O cosseno de {}º é {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print ('A tangente de {}º é {:.2f}'.format (angulo, tangente))
