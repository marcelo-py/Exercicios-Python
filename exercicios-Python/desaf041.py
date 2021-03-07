from datetime import date
nascimento = int(input('Data de nascimento: '))
atual = date.today().year
idade = atual - nascimento
print('O atleta tem {} anos de idade'.format(idade))
if idade <= 9:
    print('CLASSE: MIRIM')
elif idade <= 14:
    print('CLASSE: INFANTIL')
elif idade <= 19:
    print('CLASSE: JÚNIOR')
elif idade <=25:
    print('CLASSE: SÊNIOR')
else:
    print('CLASSE: MASTER')
