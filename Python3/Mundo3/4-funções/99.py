'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.'''


def maior(*n):
    i = m = 0
    while i < len(n):
        if n[i] > m:
            m = n[i]
        i += 1
    print(m)


maior(3, 5, 6, 10)
maior(3, 5, 61, 10)
maior(3, 52, 6, 10)
maior(33, 5, 6, 10)
