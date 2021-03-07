def notas(*n, sit = False):
    notas = dict()
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = sum(n)/len(n)
    if sit:
        if notas['média'] >= 7:
            notas['situação'] = 'Boa'
        if notas['média'] >= 5:
            notas['situação'] = 'Razoável'
        else:
            notas['situção'] = 'Péssimo'
    return notas

#Programa Princiapal
resp = notas(4, 5, 5, sit = True )
print(resp)