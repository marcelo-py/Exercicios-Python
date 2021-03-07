km = float(input('Qual a distância em km: '))
preço = 0.50*km
desconto = km*0.45
if preço <= 100:#200:
    #0.50*km
    print('Você pagará {}R$'.format(preço))
else:
    #0.45
    print('Você pagara com desconto {}R$'.format(desconto))

