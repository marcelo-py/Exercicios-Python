contp = contmil = total =  menor = 0
nomemenor  = ' '
while True:
    contp += 1
    print('---{}º Produto---'.format(contp))
    nomeproduto = str(input('Nome: '))
    preçoproduto = float(input('Preço: '))
    sn = str(input('Deseja continuar? [S/N]: '))
    while sn not in 'SsNn':
        sn = str(input('Deseja continuar? [S/N]: '))
    if preçoproduto > 1000:
        contmil += 1
    total += preçoproduto
    if menor == 0:
        menor = preçoproduto
    else:
        if preçoproduto < menor:
            menor = preçoproduto
            nomemenor = nomeproduto
    if sn in 'Nn':
        break
print('Total a pagar R$: {}R$'.format(total))
print('Quantidade de produtos que custam mais de 1.000R$: {}'.format(contmil))
print('O nome do menor produto é {} e custa {}R$'.format(nomemenor, menor))
