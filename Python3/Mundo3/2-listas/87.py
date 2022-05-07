'''Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''
linha=[[],[],[]]
i=e=l=par=coluna3=0
while len(linha[0])+len(linha[1])+len(linha[2])<9:
  while len(linha[i])<3:
    n=int(input("Valor: "))
    linha[i]+=n,
    if n % 2 == 0:
      par+=n
  coluna3+=n
  i+=1
while l<3:
  while e<3:
    print(f"[{linha[l][e]:^5}]",end="")
    e+=1
  print()
  l+=1
  e=0

print(f"A soma dos valores pares foi de {par}")
print(f"A soma dos valores da terceira coluna foi de {coluna3}")
print(f"O maior valor da segunda linha foi de {max(linha[1])}")