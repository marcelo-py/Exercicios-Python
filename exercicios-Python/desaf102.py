def fatorial(n, show=False):
    """
    
    :param n: O valor do Fatorial a ser calculado
    :param show: opção de mostrar o cálculo ou não
    :return: resultado do Fatorial
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f

print(fatorial(5, show=True))