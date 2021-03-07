seg1 = float(input('Primeiro segmento'))
seg2 = float(input('Segundo segmento'))
seg3 = float(input('Terceiro segmento'))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:  #dica: a soma dos dois menores tem que ser maior que o que ficar de fora da soma
    print('Podem formar um triangulo ',end='')
    if seg1 == seg2 == seg3: #TODOS SEGUIMENTOS IGUAIS (EQUILATERO)
        print('EQUILATERO')
    elif seg1 != seg2 != seg3 != seg1: #TODOS OS SEGNMENTOS DIFERENTES
        print('ESCALENO')
    else:
        print('ISÒCELES') #DOIS SEGMENTOS IGUAIS E UM DIFERENTE
else:
    print('Os segmentos não podem formar um triangulo')
