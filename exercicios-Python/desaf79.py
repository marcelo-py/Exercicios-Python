numero = []
while True:
    numeros = int(input('Digite um número '))
    if numeros not in numero:
        numero.append(numeros)
        numero.sort()
    else:
        print('Valor duplicado! Ignorado')
    sn = str(input('Deseja continuar? [S/N]: '))
    while not sn in 'SsNn':
        sn = str(input('Deseja continuar? [S/N]: '))
    if sn in 'Nn':
        break
print(numero)
