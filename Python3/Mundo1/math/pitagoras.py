from math import hypot

a = int(input("Comprimento do cateto oposto: "))
b = int(input("Comprimento do cateto adjacente: "))

c = hypot(a,b)

print("O comprimento da hipotenusa é: {}".format(c))
