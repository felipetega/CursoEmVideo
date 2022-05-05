maior = 0
menor = 0
for c in range(1,8):
    idade = int(input(f"Digite sua idade, {c}: "))
    if idade>=18:
        maior = maior + 1
    else:
        menor = menor + 1

print(f"O total de maiores é {maior}")
print(f"O total de menores é {menor}")
