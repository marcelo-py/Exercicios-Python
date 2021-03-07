expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha)> 0:    #quer dizer que ja tem um e deve ser fechado # aqui se for maior que 0 quer dizer que ja tem um (   #um ) só vai fechar se o outro sumir
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')
