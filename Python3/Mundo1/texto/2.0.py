nome = str(input("Digite seu nome: ")).upper().strip()
print("Seu nome possui quantas letras? {}".format(len(nome)-nome.count(" ")))
print("Possui quantos 'e': {}".format(nome.count("E")))
