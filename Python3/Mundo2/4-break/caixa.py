'''Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''
cinquenta = vinte = dez = um = 0
saque = int(input("Que valor deseja sacar? "))
while saque >= 50:
    saque -= 50
    cinquenta += 1
while saque >= 20:
    saque -= 20
    vinte += 1
while saque >= 10:
    saque -= 10
    dez += 1
while saque < 10 and saque != 0:
    saque -= 1
    um += 1
print(f"Notas de 50: {cinquenta}\nNotas de 20: {vinte}\nNotas de 10: {dez}\nNotas de 1: {um}")
