'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

totalgasto = maisdemil = 0
ls_produtos = []
while True:
    nome = " "
    nome = str(input("Nome do produto: ")).strip().upper()
    preço = int(input("Preço do produto: "))
    totalgasto += preço
    ls_produtos += [preço]
    if preço > 1000:
        maisdemil += 1
    resposta = " "
    while resposta not in "SN":
        resposta = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if resposta == "N":
        print(f"O total gasto foi de: {totalgasto}")
        print(f"O número de produtos que custaram mais de 1000 reais foi de: {maisdemil}")
        print(f"O produto mais barato custou: {min(ls_produtos)}")
        break
