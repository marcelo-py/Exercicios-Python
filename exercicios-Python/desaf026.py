nome = str(input('Digite uma frase para analise ')).strip().lower().replace('ã', 'a').replace('á', 'a').replace('â', 'a')
numero = nome.count('a')
primeiro = nome.find('a')+1
ultimo = nome.rfind('a')+1
print('A frase {}, contem {} letra A \nA primeira letra A aparece na posição {} e a ultima na posição {}'.format(nome, numero, primeiro, ultimo ))
