salario = float(input('qual o salario atual R$:'))
reajuste = salario + (salario*15/100)
adicional = salario + (salario*15/100)- salario
print ('O valor do salario que custava {}R$, com um aumento de 15%, agora vai valer {:.2f}R$ com um adicional de {:.2f} '.format (salario, reajuste, adicional))
