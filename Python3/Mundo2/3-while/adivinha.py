'''
Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 1 e 5.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

tentativa = 1

x = int(input("Pensei em um número de 1 a 5... Adivinhe qual: "))
y = randint(1,5)
while x != y:
    tentativa += 1
    print(f"Errou! Eu pensei no número {y} e vc disse {x}")
    y = randint(1,5)
    x = int(input("Pensei em um número de 1 a 5... Adivinhe qual: "))
print(f"ACERTOU, seu número de tentativas foi {tentativa}")
