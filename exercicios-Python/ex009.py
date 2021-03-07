n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro:'))
a = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 // n2
di = n1 ** n2
print ('A soma é {}, o produto é {}'.format(a, m), end='>>>')
print ('A divisão é {:.3f} a divisão inteira é {} \n e a potência é{}'.format(d, p, di))
