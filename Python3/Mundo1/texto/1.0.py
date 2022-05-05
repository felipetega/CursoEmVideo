from itertools import count


nome = str(input("Digite seu nome: ")).strip().upper()
print("Seu nome começa com 'Fe'? {}".format("FE" in nome[:2]))
print("Seu nome tem 'Ribeiro'? {}".format("RIBEIRO" in nome))
print("Seu nome tem {} letras".format(len(nome)-nome.count(" ")))
print("Seu nome tem {} letras 'e'".format(nome.count("E")))
print("A primeira letra 'e' aparece na posição {}".format(nome.find("E")+1))
print("A última letra 'e' aparece na posição {}".format(nome.rfind("E")+1))
