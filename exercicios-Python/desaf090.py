resultado = dict()
resultado['nome'] = str(input('Nome do aluno: '))
resultado['média'] = float(input('Média de {} '.format(resultado['nome'])))
if resultado['média'] < 7:
    resultado['situação'] = 'REPROVADO'
if resultado['média'] >= 7:
    resultado['situação'] = 'APROVADO'
for k, c in resultado.items():
    print('- {} é igual a {}'.format(k, c))