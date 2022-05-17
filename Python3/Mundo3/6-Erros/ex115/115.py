from function import *

arq = "cursoemvideo.txt"

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    menu = int(input(
        "MENU PRINCIPAL\n1-Ver pessoas cadastradas\n2-Cadastrar novas pessoas\n3-Sair\n"))
    if menu == 1:
        lerArquivo(arq)
    elif menu == 2:
        nome = str(input("Nome: "))
        idade = int(input("Idade: "))
        cadastrar(arq, nome, idade)
    elif menu == 3:
        break
    else:
        print("ERRO")
