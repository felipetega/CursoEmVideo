'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
lista=[]
maior=0
menor=0
for c in range(0,5):
    n=int(input(f"Digite um número na posição {c+1}: "))
    lista+=n,
    if n == max(lista):
        maior = c
    elif n == min(lista):
        menor = c
print(f"O menor valor da lista é: {min(lista)}, e está na posição {menor+1}")
print(f"O maior valor da lista é: {max(lista)}, e está na posição {maior+1}")
