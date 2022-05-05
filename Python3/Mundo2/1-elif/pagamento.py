p = float(input("Digite o valor do produto: "))
print("ESCOLHA A FORMA DE PAGAMENTO:")

f = int(input("1- Á vista\n2- Parcelado em até 3x\n3-Parcelado em 4x ou mais\n"))
if f==1:
    print("Desconto de 10%, valor do produto {}".format(p*0.9))
elif f==2:
    print("Desconto de 5%, valor do produto {}".format(p*0.95))
elif f==3:
    print("Juros de 5%, valor do produto {}".format(p*1.05))
##while f!= 1 or 2 or 3:
    ##return

