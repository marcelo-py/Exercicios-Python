casa = float(input('Qual o valor da casa? :'))
salario = float(input('Quanto você ganha? '))
anos = int(input('Em quantos anos deseja pagar?'))
preço = casa/(anos*12)
valor = salario * 30 / 100
print('o preço da prestação será {:.2f}'.format (preço))
if preço <= valor:
    print('voce conseguiu aprovar seu empréstimo')
else:
    print('Que pena empréstimo negado')
