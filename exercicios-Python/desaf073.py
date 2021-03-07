tabela = ('São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Grêmio', 'Palmeiras', 'Fluminense', 'Santos',
          'Ceará', 'Corinthians', 'Athletico-PR', 'Atlético-GO', 'Bragantino', 'Sport', 'Vasco', 'Fortaleza')
while True:
    opç = str(input('''Escolha uma opção
    a) Tabela de classificação
    b) Ver a posição do seu time
    c) Ver os times em ordem alfabetica
    d) para sair'''))
    while not opç in 'AaBbCcDd':
        print('Digite uma opção valida')
        opç = str(input('''Escolha uma opção
    a) Tabela de classificação
    b) Ver a posição do seu time
    c) Ver os times em ordem alfabetica
    0) para sair''')).lower()
    if opç == 'a':
        print(tabela)
    if opç == 'b':
        nometime = str(input('Digite o nome do seu time')).capitalize()
        print(tabela.index(nometime)+1)
    if opç == 'c':
        print(sorted(tabela))
    if opç == 'd':
        break
print('Falow, até a próxima!')

#print(tabela[0:5])


#print(tabela[-4:])
#print(sorted(tabela))
#print(tabela.index('Sport')+1)
