nome = str(input("Digite seu nome completo: ")).strip().title()

print("Primeiro nome: {}".format(nome.split()[0]))
print("Último nome: {}".format(nome.split()[-1]))
