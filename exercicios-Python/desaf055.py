maior = 0
menor = 0
for c in range(1,6):
    peso = float(input('{}º peso'.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('Maior é: \033[34m{}\033[m'.format(maior))
print('Menor é: \033[32m{}'.format(menor))
