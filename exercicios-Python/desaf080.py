lista = []
for c in range(0,5):
    num = int(input('Digit um número'))
    if num == 0 or num > lista[-1]:
        lista.append(num)
        print('Adcionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print('Adcionado a posição {} da lista '.format(pos))
                break
            pos+=1
print('Os valores digitados em ordem foram {}'.format(lista))
