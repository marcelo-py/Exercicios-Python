soma = 0
velho = 0
nomevelho = ''
mulher20 = 0
for p in range(1,5):
    print('-----{}ª pessoa-----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    soma += idade
    if p == 1 and sexo in 'Mm':
        velho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print('A média de idade das 4 pessoas é {}'.format(soma/4))
print('O homem mais velho tem {} anos e e chama {}'.format(velho, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(mulher20))
