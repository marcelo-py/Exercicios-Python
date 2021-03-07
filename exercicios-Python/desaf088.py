from random import randint
lista = list()
jogos = list()
quantos = int(input('Quantos jogos deseja? '))
total = 0
while total < quantos:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
            if cont >= 6:
                break
    total += 1
    jogos.append(lista[:])
    lista.clear()
for i, j in enumerate(jogos):
    print('Jogo {}: {}'.format(i+1, j))
