def maior(*num):
    print('\033[1;35mAnalizando os numeros \033[m')
    cont = 0
    for f in num:
        print('\033[1; 7;32m{}'.format(f),end=' ')
        cont += 1
    print('\033[1;34mForam informados {} vlores '.format(cont))
    print('\033[1;32m- O maior número informado foi {}'.format(max(num)))


#Programa principal
maior(1, 5, 15, 20, 50, 10, 8)
maior(9, 2, 3)
maior(3, 7, 6, 13)
maior(12, 0, 90)