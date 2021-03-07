print('\033[1;34m{:=^40}\033[m'.format('LOJAS MARCELO'))
preço = float(input('Preço da compra: '))
dinchek = preço - (preço * 10)/100
avistacard = preço - (preço * 5)/100
parcelado = preço / 2
print('FORMAS DE PAGAMENTO')
print('[1] á vista dinheiro/cheque')
print('[2] á vista no cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')
opção = int(input('Qual é a opção? '))
print('='*20)
print('O preço é R${}'.format(preço))
if opção == 1:
    print('O valor á vista no dinheiro/cheque é R${}'.format(dinchek))
elif opção == 2:
    print('O valor á vista no cartão é R${}'.format(avistacard))
elif opção == 3:
    print ('O preço de 2x no cartão é R${:.2f} com a parcelas de {:.2f} '.format(preço, parcelado))
elif opção == 4:
    vezes = int(input('quer parcelado em quantas vezes?'))
    valor = preço + (preço*20)/100
    parcela = valor / vezes
    print('A escolha foi de {}x a parcela com jurus será de R${:.2f} '.format(vezes, parcela))
    print('O valor final será de R${:.2f}'.format(valor))
