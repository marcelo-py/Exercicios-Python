n1 = int(input('Digite um numero'))
n2 = int(input('Digite outro número'))
n3 = int(input('Mais um numro'))
n4 = int(input('Agora o último numero'))
lista = (n1, n2, n3, n4)
print('os números digitados foram {}'.format(lista))
print('O número 9 apareceu {}x'.format(lista.count(9)))
if 3 in lista:
    print('O numero 3 aparece primeiro na  posição {}'.format(lista.index(3)+1))
else:
    print('O valor 3 não foi digitado nenhuma vez')
print('Os valores pared digitados foram',end=' ')
for n in lista:
    if n % 2 == 0:
        print('{}'.format(n),end=' ')
