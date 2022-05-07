'''Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''
lista = []
i=alunos=individual=0
while True:
  lista.append([])
  nome=str(input("Nome: "))
  nota1=int(input("Nota 1: "))
  nota2=int(input("Nota 2: "))
  lista[i]+=nome, nota1, nota2
  i+=1
  next=str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
  if next=="N":
    break
while alunos<i:
  print(f"A média do aluno {lista[alunos][0]} é de {(lista[alunos][1]+lista[alunos][2])/2}")
  alunos+=1
individual=str(input("Deseja ver as notas individualmente? ")).upper().strip()[0]
if individual=="S":
  alunos=0
  while alunos<i:
    print(f"Nome: {lista[alunos][0]}; Nota1: {lista[alunos][1]}; Nota2: {lista[alunos][2]}")
    alunos+=1
