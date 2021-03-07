num = int(input('Digite um numero: '))
total = 0
for c in range(1,num+1):    #o numero só tem que ser divisivel por 1 e por ele mesmo, ou seja divisivel duas vezes de forma inteira para cada valor distribuido
    if num % c==0:
        total += 1
        print('\033[34m',end='') #condição, situação do if cor somente para guiar com base na formula
    else:
        print('\033[31m',end='')
    print('{}'.format(c),end=' ') #será  mostrado sempre que for a hora de mostrar o for c
print('\n\033[mO numero {} foi divisivel {}'.format(num, total))
if total == 2:
    print('E por isso ele é um número PRIMO')
else:
    print('E por isso ele é um numero COMPOSTO e não primo')
