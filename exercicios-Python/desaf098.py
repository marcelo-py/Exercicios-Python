from time import sleep
def contador(i, f, p):
    print('Contagem de {} até {} pulando de {} em {}'.format(i, f, p, p))
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i <= f:
        cont = i
        while cont <= f:
            print(cont, end=' ')
            cont += p
            sleep(0.5)
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(cont,end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')
#programa principal
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar')
ini = int(input('Inicio: '))
fim = int(input('Final:  '))
raz = int(input('Passo:  '))
contador(ini, fim, raz)