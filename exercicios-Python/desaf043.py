peso = float(input('\033[1;33mDigite o peso: \033[m'))
altura = float(input('\033[1;34mDigite a altura:\033[m'))
imc = peso/(altura**2)
print('\033[1;7;32mO IMC dessa pessoa é\033[m  \033[1;7m{:.1f}\033[m'.format(imc))
if imc < 18.5:
    print('\033[1;35mEssa pessoa está abaixo do peso')
elif imc < 25:
    print('\033[1;35mEssa pessoa tem o peso ideal')
elif imc <30:
    print('\033[1;32mSobrepeso')
elif imc < 40:
    print('\033[1;36mObesidade')
else:
    print('\033[1;32mObesidade Mórbida')
