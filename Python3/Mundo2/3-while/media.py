'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

from timeit import repeat


resposta = "S"
lista = []
contador = 0
while resposta == "S":
    x = int(input("Digite um número: "))
    lista += [x]
    contador += 1

    resposta = str(input("Deseja continuar?[S/N]: ")).strip().upper()
    if resposta == "S":
        repeat
    elif resposta == "N":
        print(f"A média dos valores foi de: {sum(lista)/len(lista)}")
        print(f"O maior valor foi: {max(lista)}, o menor valor foi: {min(lista)}")
