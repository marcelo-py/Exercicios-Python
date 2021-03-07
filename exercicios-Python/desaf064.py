num = 0
soma = 0
cont = 0
while num != 999:
    num = int(input('Digite um numero inteiro (999 para parar)')) # ou  posso jogar essa linha copiada pra cima do while e copiar em baixo tbm
    cont += 1
    soma += num
    #copiar ela aqui que vai desconsiderar um contador e o 999
print('Processo finalizado! a soma entre os {} numeros da {}'.format(cont-1, soma-999))
