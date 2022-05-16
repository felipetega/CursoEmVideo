'''Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''
from uteis import dobro, metade, aumento, reducao

x=int(input("Número inteiro: "))

print(f"O dobro de {x} é {dobro(x)}")
print(f"A metade de {x} é {metade(x)}")
print(f"110% de {x} é {aumento(x)}")
print(f"90% de {x} é {reducao(x)}")