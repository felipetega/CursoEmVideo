'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
c=0
par=tupla=()
while c<4:
    x=int(input(f"{c+1}- Digite um valor: "))
    tupla+=x,
    c+=1
    if x % 2 == 0:
        par+=x,
print(f"O número 9 apareceu {tupla.count(9)} vez(es)")
print(f"O número 3 apreceu primeiro na posição {tupla.index(3)+1}")
print(f"Os números pares foram: {par}")
