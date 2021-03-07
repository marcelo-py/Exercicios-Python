largura = float(input('digite a largura de sua parede: '))
altura = float(input('Agora digite a altura: '))
s = (largura * altura)/2
print ('Sua parede tem dimensão de {}x{} e sua àrea é de {}m². Para pintar sua parede, você precisará de {}L de tinta'.format (largura, altura, largura*altura, s ))
