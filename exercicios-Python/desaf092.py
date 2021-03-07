""""Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. 
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar"""""
from datetime import date
relação = dict()
relação['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
relação['idade'] = date.today().year - ano
relação['ctps'] = int(input('Carteira de trabalho (0 para não tem): '))
if relação['ctps'] == 0:
    for c, v in relação.items():
        print('{} tem o valor {}'.format(c, v))
if relação['ctps'] != 0:
    relação['contratado'] = int(input('Ano de contratação: '))
    relação['salário'] = float(input('Salário: '))
    relação['aposentadoria'] = relação['idade'] + (relação['contratado'] +35) - date.today().year
    for c, v in relação.items():
        print('{} tem o valor {}'.format(c, v))
