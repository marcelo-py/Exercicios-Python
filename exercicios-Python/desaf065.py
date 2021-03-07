resp = 's'
quantidade = soma = maior = menor = 0
while resp in 'Ss':
    num =  int(input('Digite um número '))
    soma +=  num
    quantidade += 1
    resp = str(input('Deseja continuar? [S/N]'))
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print('A média entre os {} digitados é {}'.format(quantidade, soma/quantidade))
print('O maior numero é {} e o menor é {}'.format(maior, menor))
