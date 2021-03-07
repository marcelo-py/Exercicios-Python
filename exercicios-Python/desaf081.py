numeros = []
while True:
    numeros.append(int(input('Digite um número ')))
    sn = str(input('Deseja continuar? [S/N]: '))
    if not sn in 'SsNn':
        sn = str(input('Deseja continuar? [S/N]: '))
    if sn in 'Nn':
        break
print('Foram {} numeros digitados'.format(len(numeros)))
numeros.sort(reverse=True)
print('Em ordem decrescente é {} '.format(numeros))
if 5 in numeros:
    print('O número 5 está incluso na lista!')
else:
    print('O número 5 não está na lista!')