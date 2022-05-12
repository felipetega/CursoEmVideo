'''Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota                                                                                                                                                              – A média da turma 
– A situação (opcional)'''

def notas(*n, situacao=True):
    print(f"Foram cadastradas {len(n)} notas")
    print(f"A maior nota foi: {max(n)}")
    print(f"A menor nota foi: {min(n)}")
    c = total = 0
    while c < len(n):
        total += n[c]
        c += 1
    media = total/c
    print(f"A média foi: {media}")
    if situacao:
      c=0
      while c<len(n):
        if n[c]>=6:
          situacao="APROVADO"
        else:
          situacao="REPROVADO"
        print(f"Nota {c+1}- {situacao}")
        c+=1



notas(3, 5, 4, 1, 8, 9, 7)









'''def notas(*n):
  lista = []
  c = 0
  while True:
    nota = int(input(f"Nota {c+1}: "))
    lista += nota,
    c += 1
    next = str(input("Continuar? [S/N]: ")).strip().upper()[0]
    if next == "N":
      break
    print(f"Foram cadastradas {len(lista)} notas")
    print(f"A maior nota foi: {max(lista)}")
    print(f"A menor nota foi: {min(lista)}")
    c = total = 0
    while c < len(lista):
        total += lista[c]
        c += 1
    media = total/c
    print(f"A média foi: {media}")

notas(3, 5, 4, 1, 8, 9, 7)
'''