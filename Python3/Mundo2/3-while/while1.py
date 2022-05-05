##parimpar
n = 1
par = -1
impar = 0
print("Digite '0' se quiser terminar")
while n != 0:
    n = int(input("Digite um número: "))
    if n % 2 ==0:
        print("PAR")
        par = par + 1
    else:
        print("IMPAR")
        impar = impar + 1
print("Acabou")
print(f"Você digitou {par} números pares, e {impar} números ímpares")
