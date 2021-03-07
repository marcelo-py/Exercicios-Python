dias = float(input('Quantos dias alugado? '))
km = float (input('Quantos km rodado?'))
valor = (dias*60) + (km*0.15)
print ('O valor total a pagar é de:{:.2f}'.format (valor))
