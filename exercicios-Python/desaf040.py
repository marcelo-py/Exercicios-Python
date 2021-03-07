nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota'))
media = (nota1 + nota2)/2
print('Tirando as notas {} e {} tem a média {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('O aluno passou')
elif media <5:
    print('O aluno está reprovado')
elif media <= 6.9: #ou media >= 5 and media  <7
    print('O aluno está de recuperação')
