sal = int(input("Digite o salário: "))
if sal <= 1250:
    print("Seu salário aumentou para {}".format(sal*1.15))
else:
    print("Seu salário aumentou para {}".format(sal*1.10))
