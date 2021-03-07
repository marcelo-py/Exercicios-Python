from datetime import date
total = 0
total2 = 0
for c in range(1,8):
    nascimento = int(input('Ano de nascimento da {}º pessoa'.format(c)))
    idade = nascimento + 18
    if date.today().year - nascimento >= 18 :
        total += 1
    else:
        total2 += 1
print('Há um total de {} pessoas menores de idade'.format(total2))
print('Há um total de {} pessoas maiores de idade'.format(total))
