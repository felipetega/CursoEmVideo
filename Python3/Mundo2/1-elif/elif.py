casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite sua renda mensal: "))
tempo = int(input("Anos para o pagamento: "))

if casa/(tempo*12) < salario*0.3:
    print("Acesso ao crédito garantido")
elif casa/tempo*12 > salario*0.3:
    print("Acesso negado")
