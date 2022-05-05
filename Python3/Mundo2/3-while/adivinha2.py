'''
Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 1 e 100.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

tentativa = 1

x = int(input("Pensei em um número de 1 a 100... Adivinhe qual: "))
y = randint(1,100)

while x != y:
    tentativa += 1
    if y>x:
        x = int(input(f"Errou! Eu pensei em um número maior do que {x}: "))
    elif y<x:
        x = int(input(f"Errou! Eu pensei em um número menor do que {x}: "))

print(f"ACERTOU, seu número de tentativas foi {tentativa}")
