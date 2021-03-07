frase = str(input('Digite uma frase: ')).upper().replace(' ','')
nome = frase[::-1]
if frase == nome:
    print('{} {}'.format(frase, nome))
    print('É um Palíndromo')
else:
    print('{}  {}'.format(frase, nome))
    print('Não é um palíndromo')


'''palavras = frase.split()         #vai separar e juntar com o join, pode ser com ifen asteriscos etc
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto)-1, -1, -1):      #vai ler de trás pra frente, começando no final indo até o fim da frase
    inverso += [junto]
print(junto)'''