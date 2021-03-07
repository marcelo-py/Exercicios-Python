soma = 0
conta = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma = soma + c #ou soma += c
        conta = conta +1 #conta += 1
print('A soma de {} valores solicitados  é {}'.format(conta, soma))
