'''Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''
dici={}
c=gols=0
dici["Nome"]=str(input("Nome: "))
dici["Partidas"]=int(input("Partidas: "))
while c<dici["Partidas"]:
  gols+=int(input(f"Gols na partida {c+1}: "))
  c+=1
dici["Gols"]=gols
for k, v in dici.items():
  print(f"{k}: {v}")
