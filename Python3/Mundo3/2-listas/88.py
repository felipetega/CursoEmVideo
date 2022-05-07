'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
lista=[]
c=i=p=0

cartelas=int(input("Quantos jogos serão gerados? "))
while c<cartelas:
  lista.append([])
  c+=1

while i<cartelas:
  while len(lista[i])<6:
    n=randint(0,60)
    if n not in lista[i]:
      lista[i]+=n,
  i+=1
while p<len(lista):
  print(lista[p])
  p+=1