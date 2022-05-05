a = int(input("Valor 1: "))
b = int(input("Valor 2: "))
c = int(input("Valor 3: "))
if a > b and a > c:
    print("Maior valor {}".format(a))
if b > a and b > c:
    print("Maior valor {}".format(b))
if c > a and c > b:
    print("Maior valor {}".format(c))

if a < b and a < c:
    print("Menor valor {}".format(a))
if b < a and b < c:
    print("Menor valor {}".format(b))
if c < a and c < b:
    print("Menor valor {}".format(c))
