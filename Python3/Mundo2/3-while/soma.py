soma = 0
x = 0
while x != 999:
    x = int(input("Digite um número para somar: "))
    soma = soma + x
if x == 999:
        soma = soma - 999
        print(soma)
