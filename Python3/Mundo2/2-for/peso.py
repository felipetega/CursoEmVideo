lista = []
for c in range(1,6):
    peso = int(input(f"Número {c}, digite seu peso: "))
    lista = lista + [peso]
print("O maior peso foi de: ",max(lista))
print("O menor peso foi de: ",min(lista))

