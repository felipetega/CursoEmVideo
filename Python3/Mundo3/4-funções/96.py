'''Exercício Python 096: Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.'''

def area(x, y):
  a=x*y
  print(f"A área do terreno é de {a}m quadrados")

x=int(input("ALTURA: "))
y=int(input("LARGURA: "))
area(x, y)