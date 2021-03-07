pessoas = conti = conth = contm = 0
while True:
    pessoas += 1
    print('{}ª Pessoa'.format(pessoas))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: '))
    sn = str(input('Deseja continuar? [S/N]'))
    while sn not in 'SsNn':
        sn = str(input('Deseja continuar? [S/N]'))
    if sexo in 'Ff':
        if idade < 20:
            contm += 1
    if sexo in 'Mm':
        conth += 1
    if idade > 18:
        conti += 1
    if sn in 'Nn':
        break
print('\033[1;32mHá {} pessoas maiores de 18 anos'.format(conti))
print('\033[1;34m{} Homens cadastrados'.format(conth))
print('\033[1;35mE {} mulheres com menos de 20 anos'.format(contm))
