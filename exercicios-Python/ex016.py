preço = float(input('Digite o preço R$ '))
desconto = preço - (preço*50/100)
lucro = preço + (preço*50/100)-preço
print ('O produto que custava {}R$, com um desconto de 50%, agora vai custar {}R$'.format (preço, desconto))
print('~'*30)
print ('o lucro é de {}'.format(lucro))
