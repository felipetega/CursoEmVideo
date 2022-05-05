'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Palmeiras.
'''

''' Peguei em ordem alfabética... Mandei o shuffle

from random import shuffle
lista = ["América Mineiro","Athlético Paranaense","Atlético Goianiense","Atlético Mineiro","Avaí","Botafogo","Ceará","Corinthians","Coritiba","Cuiabá","Flamengo","Fluminense","Fortaleza""EC","Goiás","Internacional","Juventude","Palmeiras","RB","Bragantino","Santos","São Paulo"]
shuffle(lista)
print(lista)
'''

tabela = ['Santos', 'Goiás', 'Botafogo', 'RB', 'Atlético Goianiense', 'Palmeiras', 'FortalezaEC', 'Cuiabá', 'Coritiba', 'Juventude', 'Athlético Paranaense', 'Atlético Mineiro', 'Avaí', 'São Paulo', 'Internacional', 'Bragantino', 'Corinthians', 'Flamengo', 'América Mineiro', 'Fluminense']
c=0
print("==================== G5 ====================")
while c<=4:
    print(f"{c+1}- {tabela[c]}")
    c+=1
print("================ LANTERNAS =================")
c=16
while c<=19:
    print(f"{c+1}- {tabela[c]}")
    c+=1
print("============= ORDEM ALFABÉTICA =============")
print(sorted(tabela))
print("=========== POSIÇÃO DO PALMEIRAS ===========")
print(tabela.index("Palmeiras")+1)

'''
print("==================== G5 ====================")
print(tabela[0:5])
print("================ LANTERNAS =================")
print(tabela[-4:])
'''
