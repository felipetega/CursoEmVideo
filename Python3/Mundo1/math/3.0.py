x = int(input("Digite um número inteiro: "))
print("O dobro do número digitado é {}".format(x*2))

b = int(input("Qual o comprimento do cateto oposto? "))
c = int(input("Qual o comprimento do cateto adjacente? "))
a2 = b*b + c*c
a = a2**0.5
print("O valor da hipotenusa do triângulo é {}".format(a))
