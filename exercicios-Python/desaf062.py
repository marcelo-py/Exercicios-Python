primeiro = int(input('Primeiro termo'))
razão = int(input('Digite a razão'))
termos = int(input('Quantos termos deseja mostrar?'))
termo = primeiro
cont = 1
mais = termos
total = 0
sn = ''
while mais != 0:
    total += mais
    while cont <= total:
        print('\033[1;34m{}'.format(termo),end=' >\033[m ')
        termo += razão
        cont += 1
    print('\033[1;33mPAUSA\033[m')
    mais = int(input('\033[1mQuantos termos dseja mostrar a mais?'))
while sn != 'n':
    sn = str(input('\n\033[1mDeseja mostrar sua progressão completa? [S/N] ')).lower()
    if sn == 's':
        for c in range(primeiro, termo, razão):
            print('\033[1;34m{} > \033[m'.format(c), end='')
        print('\033[1;35mFIM!\033[m')
    if sn != 's' and sn != 'n':
        print('\033[1;32mOpção invalida!!!\033[m')
print('\nProgressão finalizada com \033[1;32m{}\033[m \033[1mtermos mostrados '.format(total))
