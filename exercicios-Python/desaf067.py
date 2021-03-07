print('=====TABUADA=====')
while True:
    num = int(input('Qual numero deseja ver a tabuada?'))
    print('='*20)
    if num < 0:
        break
    for c in range(1, 11):
        print('{} x {} = {}'.format(num, c, num * c))
    print('='*20)
print('TABUADA FINALIZADA!')
