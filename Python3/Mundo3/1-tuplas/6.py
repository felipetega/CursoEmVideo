'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

from timeit import repeat
produtos=preços=()
while True:
    produto=str(input("Digite o NOME do produto: ")).strip().upper()
    preço=int(input("Digite o PREÇO do produto: R$"))
    produtos+=produto,
    preços+=preço,
    next=str(input("[S/N] Deseja continuar? ")).strip().upper()[0]
    if next == "S":
        repeat
    else:
        break

c=0
print(f"PRODUTOS        --- PREÇOS")
while c != len(produtos):
    print(f"{produtos[0+c]:15} --- R${preços[0+c]:.2f}")
    c+=1
