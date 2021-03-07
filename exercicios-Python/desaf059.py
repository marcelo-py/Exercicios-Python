from time import sleep
num1 = int(input('Primeiro valor'))
num2 = int(input('Segundo valor'))
opção = 0
while opção != 5:
    print("""    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair""")
    print('='*20)
    opção = int(input('Qual sua opção?'))
    if opção == 1:
        soma = num1 + num2
        print('{} + {}  da {}'.format(num1, num2, soma))
    if opção == 2:
        multiplicar = num1 * num2
        print('O resultado entre {} x {} é {}'.format(num1, num2, multiplicar))
    if opção == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('Entre {} e {} o maior é {}'.format(num1, num2, maior))
    if opção == 4:
        print('Informe os numeros novamente')
        num1 = int(input('Primeiro valor'))
        num2 = int(input('Segundo valor'))
    print('='*20)
print('Finalizando Programa...')
sleep(2)
print('Programa finalizado!!!')