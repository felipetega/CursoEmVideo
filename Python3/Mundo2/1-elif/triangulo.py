a = int(input("Lado 1: "))
b = int(input("Lado 2: "))
c = int(input("Lado 3: "))
if a>=b+c or b>=a+c or c>=a+b:
    print("NÃO FORMA TRIÂNGULO")
else:
    print("FORMA TRIÂNGULO", end=" ")
    if a==b==c:
        print("EQUILÁTERO")
    elif a==b or a==c or b==c:
        print("ISÓSCELES")
    elif a!=b!=c:
        print("ESCALENO")
