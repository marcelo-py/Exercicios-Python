nome = str(input('Digite seu nome')).strip()
nome1 = nome.split()
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu ultimo nome é {}'.format(nome1[len(nome1)-1]))
