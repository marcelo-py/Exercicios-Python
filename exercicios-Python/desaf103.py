def ficha(nome = '<desconhecido>', gols = 0):
    print('O jogador {} fez {} gols'.format(nome, gols))

#programa principal
n = str(input('Nome do jogador: '))
g = str(input('Quantos gols feitos? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '': # Isto é, tirou todos os espaços e ficou vazio...
    ficha(gols= g) #Só tem que mostrar  os gols
else:
    ficha(n, g)