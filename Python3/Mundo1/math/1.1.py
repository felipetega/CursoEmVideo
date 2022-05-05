from cmath import sqrt
from math import cos, sin, tan, radians
ang = float(input("Digite um ângulo: "))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print("Seno é {:.2f}, cosseno é {:.2f}, tangente é {:.2f}".format(seno,cosseno,tangente))

b = int(input("Cateto oposto: "))
c = int(input("Cateto adjacente: "))

a2 = (b**2) + (c**2)
a = a2**(1/2)

print("O valor da hipotenusa é {:.2f}!".format(a))
