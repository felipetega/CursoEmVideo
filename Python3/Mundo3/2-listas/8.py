'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas. 
C) Uma listagem com as pessoas mais leves.
'''

listaNome = listaPeso = []
maiorPeso = menorPeso = c = posMaiorPeso = posMenorPeso = 0
while True:
    nome=str(input("Nome: "))
    listaNome+=nome,
    peso=int(input("Peso: "))
    c+=1
    if maiorPeso < peso:
        maiorPeso=peso
        posMaiorPeso=c
    if menorPeso == 0:
        menorPeso = peso
        posMenorPeso=c
    elif menorPeso > peso:
        menorPeso = peso
        posMenorPeso=c
    next=str(input("Continuar? [S/N] ")).upper().strip()[0]
    if next == "N":
        break
print(f"O número de pessoas cadastradas foi de {c}!")
print(f"O maior peso foi de {listaNome[posMaiorPeso-1]}, pesando {maiorPeso}")
print(f"O menor peso foi de {listaNome[posMenorPeso-1]}, pesando {menorPeso}")
