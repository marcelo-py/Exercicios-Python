relação = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota'))
    nota2 = float(input('Segunda nota'))
    sn = str(input('Deseja sair? [S/N]'))
    média = (nota1 + nota2) / 2
    relação.append([nome,[nota1, nota2], média])
    if sn in 'Ss':
        break
print('Nº |  Nome  |   Média ')
for i, r in enumerate(relação):
    print('{}   {}   {}'.format(i, r[0], r[2]))
while True:
    qual = int(input('Qual nota deseja mostrar? 999 para sair '))
    while qual <0:
        qual = int(input('Qual nota deseja mostrar? 999 para sair '))
    if qual <= len(relação)-1:
        print('As notas de {} são: {}'.format(relação[qual][0], relação[qual][1]))
    if qual == 999:
        break
