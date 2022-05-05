from math import sin, cos, tan, radians

a = int(input("Digite o ângulo do triângulo: "))

cosseno = cos(radians(a))
seno = sin(radians(a))
tangente = tan(radians(a))

print("Cosseno é {:.2f}, seno é {:.2f}. tangente é {:.2f}".format(cosseno,seno,tangente))
