'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

x = 0

while True:
    if x >= 0:
        c = 1
        x=int(input("Digite um número inteiro: "))
        if x <= 0:
            print("FIM")
            break
        while c < 11:
            print(x*c)
            c += 1
