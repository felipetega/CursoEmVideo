x = int(input("Digite um número inteiro: "))
fatorial = x
resultado = 1

while fatorial != 1:
    resultado = resultado * fatorial
    fatorial = fatorial-1

print(resultado)
