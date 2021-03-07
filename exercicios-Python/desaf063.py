print('SEQUENCIA DE FIBONACCI')
num = int(input('quantos termos?'))
t1 = 0
t2 = 1
print('{} > {} >'.format(t1, t2),end=' ')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print('{} >'.format(t3),end=' ')
    cont += 1
    t1 = t2 #t1 para a ser t2
    t2 = t3 #t2 passa a ser t3  na sequencia é um tipo de transição
print('FIM')