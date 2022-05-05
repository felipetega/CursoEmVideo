'''
tupla+=x, ESSA VÍRGULA É NECESSÁRIA PARA TRANSFORMAR O X EM INT

Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''
from random import randint
from timeit import repeat
tupla=()
while True:
    if len(tupla)<5:
        x=randint(0,10)
        if x not in tupla:
            tupla+=x,
        elif x in tupla:
            repeat
    else:
        break
print(tupla)
print(f"O maior valor foi: {max(tupla)}")
print(f"O menor valor foi: {min(tupla)}")
