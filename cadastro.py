relação = dict()
menores = dict()
maiores = dict()
while True:
    nome = input('Digite seu nome ')
    if len(nome) == 0:
        break
    idade = int(input('Digite sua idade '))
    numero = int(input('Digite seu numero '))
    relação[nome] = {'idade':idade, 'numero':numero}

print('\033[1;36mTodos as pessoas em ordem alfabetica por nome')
print('-'*30)
for p in sorted(relação.items()):
    print('{}: idade: {}; numero: {}'.format(p[0], p[1]['idade'], p[1]['numero']))
print('='*30)
for m in relação:
    if relação[m]['idade'] < 18:
        menores[m] = relação[m]
    else:
        maiores[m] = relação[m]
print()
print('\033[1;32m<menores de idade>')
print('-'*30)
for m in menores.items():
    print('{}: idade: {}; numero: {}'.format(m[0], m[1]['idade'], m[1]['numero']))
print()
print('='*30)
print('\033[1;34m<maiores de idade>')
for m in maiores.items():
    print('{}: idade: {}; numero: {}'.format(m[0], m[1]['idade'], m[1]['numero']))