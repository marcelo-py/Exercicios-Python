salario = float(input('Qual o valor atual do salario R$? '))
valor = salario + ((salario*15)/100)-salario
valor2 =  salario + ((salario*10)/100) - salario
if salario <= 1250:
    print('Com o salário de R${} passa a ganhar R${} agora'.format(salario,(salario + (salario*15)/100)))
    print('Com um aumento de {}R$'.format(valor))
else:
    print('Com o salário de R${} passa a ganhar R${} agora'.format(salario, (salario + (salario*10)/100)))
    print('com um aumento de {}R$'.format(valor2))
