numeros = ('Zero', 'Um','Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
           'Trêze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
numero = 0
while numero != range(0,20):
    numero = int(input('Digite um numero pra ser lido por extensso'))
    if numero in range(0, 21):
        procurando = numeros[numero]
        print(procurando)
        break
