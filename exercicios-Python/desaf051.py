termo = int(input('Primeiro termo '))
razão = int(input('Qual a razão '))
decimo = termo +(10-1) * razão #A Formula para calcular o enesimo termo (ou seja mostrar apartir de um numero/termo seus 10 primeiras progressão, termo 5 com a razão que vai pulando por exmplo 2| 5, 7, 9... até ter 10  numeros(numero enezimo, oq foi pedido)
for c in range(termo,decimo +razão ,razão):
    print(c)
