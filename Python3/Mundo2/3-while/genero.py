'''
Exercício Python 57:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input("Dados inválidos. Digite novamente 'M' ou 'F': ")).upper().strip()[0]
while sexo not in "MF":
    sexo = str(input("Dados inválidos. Digite novamente 'M' ou 'F': ")).upper().strip()[0]
print(f"Sexo {sexo} registrado com sucesso")
confirma = str(input("Confirma as informações fornecidas? [S/N]: ")).upper().strip()[0]
while confirma not in "SN":
    confirma = str(input("Confirma as informações fornecidas? [S/N]: ")).upper().strip()[0]
    if "S" in confirma:
        print("Okay, vamos prosseguir")
    elif "N" in confirma:
        print("Dado excluído")
        break

