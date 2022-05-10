'''Exercício Python 100:
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.'''
from random import randint

numeros = []


def sorteia():
    c = 0
    while c < 5:
        numeros.append(randint(1, 21))
        c += 1


def somaPar(numeros):
    c = 0
    par = 0
    while c < 5:
        if numeros[c] % 2 == 0:
            par += numeros[c]
        c += 1
    print(f"A soma de todos os números pares de {numeros} é de {par}")


sorteia()
somaPar(numeros)
