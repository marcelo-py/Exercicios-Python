soma = cont = 0
while True:
    num = int(input('Digite um numero ou 999 para parar'))
    if num == 999:
        break
    cont += 1
    soma += num
print('A soma entre os {} numeros da {}'. format(cont, soma))

