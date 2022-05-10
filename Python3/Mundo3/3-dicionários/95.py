'''Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.'''
'''Crie um programa que gerencie o aproveitamento de VÁRIOS jogadores de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
lista = []
dici = {}
i = gols = p = 0
while True:
  lista.append({})
  lista[i]["Nome"] = str(input("Nome: "))
  lista[i]["Partidas"] = int(input("Partidas: "))
  while p < int(lista[i]["Partidas"]):
    gols += int(input(f"Gols na partida {p+1}: "))
    p += 1
  lista[i]["Gols"] = gols
  p = gols = 0
  i += 1
  next = str(input("Deseja continuar? [S/N]: ")).strip().upper()[0]
  if next == "N":
    break
i = totalGols = 0
while i<len(lista):
  print(lista[i])
  totalGols += int(lista[i]["Gols"])
  i+=1
print(f"O total de gols desses jogadores no campeonato foi de: {totalGols}")
