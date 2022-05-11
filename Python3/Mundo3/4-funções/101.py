'''Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''
def voto(idade):
    if idade == 16 or idade == 17 or idade >= 70:
        print("VOTO OPCIONAL")
    elif idade >= 18 and idade <= 69:
        print("VOTO OBRIGATÓRIO")
    else:
        print("VOTO NEGADO")


idade = int(input("Digite sua idade: "))
voto(idade)
