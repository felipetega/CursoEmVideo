x = int(input("Valor inicial: "))
y = int(input("Razão: "))
c = int(input("Contador: "))
resultado = x

while c+1 != 0:
    print(resultado, end=" ")
    resultado = resultado+y
    c = c -1
restart = int(input("\n[1] Adicionar ao contador\n[2] Sair\n"))
if restart == 1:
        c2=int(input("Quantas contagens você quer alterar? "))
        c = c + c2
        while c+1 != 0:
            print(resultado, end=" ")
            resultado = resultado+y
            c = c -1
