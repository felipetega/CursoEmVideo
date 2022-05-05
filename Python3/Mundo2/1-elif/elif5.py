n1 = int(input("Nota da primeira prova: "))
n2 = int(input("Nota da segunda prova: "))
m=(n1+n2)/2
if m<5:
    print("REPROVADO")
elif m>5 and m<6.9:
    print("RECUPERAÇÃO")
elif m>=7:
    print("APROVADO")
