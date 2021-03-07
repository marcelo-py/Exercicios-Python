from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceito nome: '))
n4 = str(input('Digite o quarto nome: '))
resultado = [n1, n2, n3, n4]
print ('A pessoa escolhida foi {}'.format (choice (resultado)))
