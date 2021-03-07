sexo = ''
s = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]')).upper().strip()
    if sexo != 'M' and sexo != 'F':
        print('Sexo invalido! por favor, ',end='')
    if sexo == 'M':
        s = 'Masculino'
    if sexo == 'F':
        s = 'Feminino'
print('Seu sexo é {}'.format(s))
