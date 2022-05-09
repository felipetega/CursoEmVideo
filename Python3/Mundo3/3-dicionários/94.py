'''Exercício Python 094:
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média'''
lista=[]
c=0
while True:
  lista.append({})
  lista[c]["Nome"]=str(input("Nome: "))
  lista[c]["Sexo"]=str(input("Sexo [M/F]: ")).strip().upper()[0]
  lista[c]["Idade"]=int(input("Idade: "))
  c+=1
  next=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
  if next == "N":
    break
print(f"Foram cadastradas {len(lista)} pessoas")
p=media=0
while p<len(lista):
  media+=int(lista[p]["Idade"])
  p+=1
print(f"A média de idade das pessoas foi de {media/c} anos")
print("\nLISTA DE MULHERES")
c=0
while c<len(lista):
  if lista[c]["Sexo"]=="F":
    print(lista[c])
  c+=1
print("\nLISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA")
c=0
while c<len(lista):
  if int(lista[c]["Idade"])>media/p:
    print(lista[c])
  c+=1
