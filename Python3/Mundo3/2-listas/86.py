'''Exercício Python 086:
Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''
linha=[[],[],[]]
i=e=l=0
while len(linha[0])+len(linha[1])+len(linha[2])<9:
  while len(linha[i])<3:
    n=int(input("Valor: "))
    linha[i]+=n,
  i+=1
while l<3:
  while e<3:
    print(f"[{linha[l][e]:^5}]",end="")
    e+=1
  print()
  l+=1
  e=0