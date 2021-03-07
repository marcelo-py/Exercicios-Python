valor = float(input('Digite o valor em dolar, euro ou real '))
dolar = valor/5.34
euro = valor/6.39
realdo = valor*5.34
reuro = valor*6.39
print ('{} R$ Compra: {:.2f} US$\n{:.2f} EUR'.format (valor, dolar, euro))
print ('-'*36)
print ('Com {} US$ voce consegue comprar: {:.2f} R$\nEur>>:{} R$ '.format (valor, realdo, reuro))
