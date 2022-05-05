'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.B) A lista de valores, ordenada de forma decrescente.C) Se o valor 5 foi digitado e está ou não na lista.'''
from timeit import repeat


lista=[]
cinco=0
contador=0
while True:
    x=int(input("Digite um número inteiro: "))
    contador+=1
    if x == 5:
        cinco+=1
    lista+=x,
    continuar=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "S":
        repeat
    else:
        break
print(f"Foram digitados {contador} valores")
lista.sort(reverse=True)
print(lista)
if cinco != 0:
    print(f"O valor cinco foi digitado {cinco} vezes e está na lista")
else:
    print("O número cinco não foi digitado")
