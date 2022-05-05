'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''
exp=str(input("Digite uma expressão: "))
if exp.count("(") == exp.count(")"):
    print("Expressão válida")
else:
    print("Expressão inválida")
