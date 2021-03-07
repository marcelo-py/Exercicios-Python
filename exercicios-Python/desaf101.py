def voto(idade):
    import datetime
    i = datetime.date.today().year - idade
    print('Com {} anos'.format(i),end=' ')
    if i > 18 and i < 70:
        return True
    else:
        return False

#Programa principal
ano = int(input('Em que ano você nasceu? '))
if voto(ano):
    print('é Obrigado a votar '.format(ano))
else:
    print('o voto é opcional '.format(ano))