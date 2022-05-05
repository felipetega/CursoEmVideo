'''Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''

tot18 = totm = totf20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totm += 1
    if sexo == "F" and idade >=20:
        totf20 += 1
    continuar = " "
    while continuar not in "SN":
        continuar = str(input("Continuar? [S/N]: ")).strip().upper()[0]
    if continuar == "N":
        print(f"Total de maiores de idade: {tot18}")
        print(f"Total de homens: {totm}")
        print(f"Total de mulheres com mais de 20 anos: {totf20}")
        break
