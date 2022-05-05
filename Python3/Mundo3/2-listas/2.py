'''
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. 
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista.sort()
'''
from timeit import repeat


lista=[]
while True:
    x=int(input("Digite um número inteiro: "))
    if x not in lista:
        lista+=x,
    continuar=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "S":
        continuar = ""
        repeat
    else:
        break
lista.sort()
print(lista)
