from uteis import dobro, metade, aumento, reducao, moeda

x=int(input("Número inteiro: "))

print(f"O dobro de {moeda(x)} é {moeda(dobro(x))}")
print(f"A metade de {moeda(x)} é {moeda(metade(x))}")
print(f"110% de {moeda(x)} é {moeda(aumento(x))}")
print(f"90% de {moeda(x)} é {moeda(reducao(x))}")