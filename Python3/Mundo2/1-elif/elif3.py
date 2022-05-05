x = int(input("Digite um número inteiro: "))
y = int(input("Digite outro número inteiro: "))
if x > y:
    print("{} é maior que {}".format(x, y))
elif y > x:
    print("{} é menor que {}".format(x, y))
elif x == y:
    print("{} e {} são iguais".format(x, y))

