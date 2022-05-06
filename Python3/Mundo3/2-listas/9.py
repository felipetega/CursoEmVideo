'''Exercício Python 085:
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''
'''impar = []
par = []

for c in range(0,7):
    n=int(input("Digite um númer inteiro: "))
    if n % 2 == 0:
        par+=n,
    if n % 2 == 1:
        impar+=n,
par.sort()
impar.sort()
print(par)
print(impar)'''

lista= [[],[]]
for c in range(0,4):
    n=int(input("Digite um númer inteiro: "))
    if n % 2 == 0:
        lista[0]+=n,
    if n % 2 == 1:
        lista[1]+=n,
print(sorted(lista[0]),sorted(lista[1]))

