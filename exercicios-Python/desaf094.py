dadosd = dict()
dadosl = list()
soma = 0
while True:
    dadosd['nome'] = str(input('Nome: '))
    dadosd['sexo'] = str(input('Sexo [M/F]: '))
    while dadosd['sexo'] not in 'MmFf':
        dadosd['sexo'] = str(input('Sexo [M/F]: '))
    dadosd['idade'] = int(input('Idade: '))
    soma += dadosd['idade']
    sn = str(input('Quer continuar? [S/N] '))
    while sn not in 'SsNn':
        sn = str(input('Erro!!! Quer continuar? S ou N? '))
    dadosl.append(dadosd.copy())
    dadosd.clear()
    if sn in 'Nn':
        break
print('Ao todo foram {} pessoas cadastradas'.format(len(dadosl)))
print('A média de idades é {}'.format(soma / len(dadosl)))
print('As mulheres cadastradas foram: ', end='')
for p in dadosl:
    if p['sexo'] == 'f':
        print(p['nome'], end=' ')
print()
print('Pessoas acima da média: ')
for p in dadosl:
    if p['idade'] > soma / len(dadosl):
        for c, v in p.items():
            print('{} = {}; '.format(c, v),end=' ')
