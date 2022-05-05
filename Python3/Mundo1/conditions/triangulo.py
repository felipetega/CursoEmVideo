a = (int(input("Reta 1: ")))
b = (int(input("Reta 2: ")))
c = (int(input("Reta 3: ")))

if a < b + c and b < a + c and c < a + b:
    print("Faz um triângulo")
else:
    print("N faz um triângulo")
