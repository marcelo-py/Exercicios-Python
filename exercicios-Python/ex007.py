soma = 0
idadehomemvelho = 0
nomevelho = ''
totalmulher20 = 0
for p in range (1,5):
    print('---{}ª Pessoa---'.format(p))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]'))
    soma += idade
    if p == 1 and sexo in 'Mm':
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadehomemvelho:
        idadehomemvelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totalmulher20 += 1
print('A média de idade do grupo é {}'.format(soma/4))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehomemvelho, nomevelho))
print('Ao todo são {} mulheres com menos de  20 anos'.format(totalmulher20))
