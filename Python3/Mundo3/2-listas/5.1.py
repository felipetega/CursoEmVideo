'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
o final, mostre o conteúdo das três listas geradas.'''

lista = []
par=[]
impar=[]
c=0
while True:
    lista.append(int(input("Digite um número inteiro: ")))
    continuar=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
while c < len(lista):
    if lista[c] % 2 == 0:
        par.append(lista[c])
    elif lista[c] % 2 == 1:
        impar.append(lista[c])
    c+=1
print(f"{lista}\n{par}\n{impar}")

