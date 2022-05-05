'''Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).'''
x = 0
ls = []
while True:
    x = int(input("Digite um número inteiro: "))
    if x == 999:
        break
    ls += [x]

print(f"Foram digitados {len(ls)} números, e a soma dos valores digitados foi de {sum(ls)}!")
