'''Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

tupla=("aveia","banana","mel","ovo","cacau")
comida=0
letra=0
a=0
e=0
i=0
o=0
u=0

print("\nCONTADOR DE VOGAIS")
while comida < len(tupla):
    print(f"\n{tupla[comida]}",end=" - ")
    while letra < len(tupla[comida]):
        if tupla[comida][letra]=="a":
            a+=1
            letra+=1
        elif tupla[comida][letra]=="e":
            e+=1
            letra+=1
        elif tupla[comida][letra]=="i":
            i+=1
            letra+=1
        elif tupla[comida][letra]=="o":
            o+=1
            letra+=1
        elif tupla[comida][letra]=="u":
            u+=1
            letra+=1        
        else:
            letra+=1
    if a != 0:
        print(f"a: {a}",end=" ")
    if e != 0:
        print(f"e: {e}",end=" ")    
    if i != 0:
        print(f"i: {i}",end=" ")
    if o != 0:
        print(f"o: {o}",end=" ")
    if u != 0:
        print(f"u: {u}",end=" ")
    a=0
    e=0
    i=0
    o=0
    u=0
    letra=0
    comida+=1
