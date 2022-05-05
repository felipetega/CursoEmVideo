from itertools import count


nome = str(input("Digite seu nome completo: ")).strip().upper()
print('Seu nome tem Silva? {}'.format("SILVA" in nome))
print("Seu nome começa com 'Lu'? {}".format(nome[0:2]=="LU"))
print("A letra 'a' aparece {} vezes na frase".format(nome.count("A")))
print("A última letra 'a' aparece na posição {}".format(nome.rfind("A")+1))
print("A primeira letra 'a' aparece na posição {}".format(nome.find("A")+1))
