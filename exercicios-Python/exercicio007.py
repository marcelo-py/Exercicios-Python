n1 = float(input('Digite sua primeira noota: '))
n2 = float(input('Digite sua segunda nota: '))
nota = (n1 + n2)/2
print('Sua media é {}'.format(nota))
print('Parabéns' if nota >=6 else 'Estude mais')
