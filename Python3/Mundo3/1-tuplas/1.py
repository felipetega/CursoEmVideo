#tuplas são imutáveis
lanche=("hamburguer","refri","batata frita","sorvete")
'''
for cont in range(0,len(lanche)):
    print(f"Eu vou comer {lanche[cont]} na posição {cont}")'''

for pos, comida in enumerate(lanche):
    print(f"Vou comer {comida} na posição {pos}")

'''
for comida in lanche:
    print(f"Vou comer {comida}")
'''
print("Comi muito!")

