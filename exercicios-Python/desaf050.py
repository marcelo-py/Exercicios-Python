soma = 0
conta = 0
for c in range(1,7):
    num = int(input('Digite o {}º valor'.format(c)))
    if num % 2==0:
        soma += num
        conta +=  1
print('A soma contem {} numeros pares e o resultado é {}'.format(conta, soma))
