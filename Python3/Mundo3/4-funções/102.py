'''Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show,
que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
def fatorial(x, show=False):
    c = f = 1
    i = 0
    lista = []
    while c <= x:
        f *= c
        lista += c,
        c += 1
    print(f"O fatorial de {x} é {f}")
    if show:
        while i < len(lista)-1:
            print(lista[i], end="x")
            i += 1
        print(x,end="=")
        print(f)


x=int(input("Digite um número para fatoriar: "))
fatorial(x)