from datetime import date
nascimento = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nascimento #voltando no tempo para mostrar a idade
print ('Quem nasceu em {} tem {} anos de idade em {}'.format(nascimento, idade, atual))
if idade < 18:                                                                                   #vai restar o que sobrou de 18
    print('ainda não está na hora, falta mais {} anos, sua data para de inscrever é {}'.format(18 - idade, 18 + nascimento)) #18 + o nascimento só vai ate quando completar 18. ex: 2000 + 18 anos
elif idade > 18:
    print('O prazo de se alistar já passou foi de {} atras, em {}'. format(idade - 18, nascimento + 18 ))
elif idade == 18:
    print('Essa pessoa deve se alistar imediatamente')



'''from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
if idade == 18:
    print('Essa pessoa deve se alistar imediatamente')
elif idade > 18:
    valor = idade - 18
    print('O prazo para quem nasceu em {} ja passou, foi {} anos atras em {}'.format(nascimento, valor, nascimento + 18))
elif idade < 18:
    valor = 18 - idade
    print ('Ainda faltam {} anos e o ano para se alistar será em {}'.format(valor, nascimento + 18))'''
