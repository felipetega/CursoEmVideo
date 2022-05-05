z=4
while z == 4 or z != [1,2,3,5]:
    x = int(input("Número inteiro 1: "))
    y = int(input("Número inteiro 2: "))
    z = int(input("O que você deseja fazer?\n[1]somar\n[2]multiplicar\n[3]maior\n[4]novos números\n[5]sair do programa\n"))

if z == 1:
    print(x+y)
elif z == 2:
    print(x*y)
if z == 3 and x>y:
    print(f"{x} é maior que o {y}")
elif z == 3 and y>x:
    print(f"{y} é maior que o {x}")
else:
    print("Saindo do programa")
