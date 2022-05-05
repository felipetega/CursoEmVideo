'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
o final, mostre o conteúdo das três listas geradas.'''
lista=[]
par=[]
impar=[]
while True:
    x=int(input("Digite um número inteiro: "))
    lista+=x,
    if x % 2 == 0:
        par+=x,
    elif x % 2 == 1:
        impar+=x,
    continuar=str(input("Deseja continuar? [S/N] ")).strip().upper()[0]
    if continuar == "N":
        break
print(lista)
print(f"Os valores pares são {par}")
print(f"Os valores impares são {impar}")
