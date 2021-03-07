#calculando fatorial de um numero

#from math import factorial
n = int(input('Digite um numero para ver seu fatorial'))
c = n
f = 1
while c > 0:
    print('{}'.format(c),end="")
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)

#com o for
''''acumulador = 1
for c in range(n, 0, -1):
    print(c, end='')
    print(' x ' if c >1 else '= ', end='')
    acumulador *= c
print(acumulador)'''''
