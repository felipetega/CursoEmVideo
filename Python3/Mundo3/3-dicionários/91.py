'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
from operator import itemgetter
from random import randint

dici = {}
pos = 1
for c in range(1, 5):
    dici["Jogador"+str(c)] = randint(1, 6)
ranking = sorted(dici.items(), key=itemgetter(1), reverse=True) ##IMPORTANTE
for pos in range(0, 4):
    print(f"{pos+1}-{ranking[pos]}")
