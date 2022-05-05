'''Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
'''
x = int(input("Quantos elementos terá sua sequência de Fibonacci? "))
n1 = 0
n2 = 1
n3 = 1
n4 = n2+n3
print(n1,end=" ")

c = 0
while c != x-1:
    n3 = n1 + n2
    print(n3, end=" ")
    n1=n2
    n2=n3
    c = c + 1
