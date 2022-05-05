a = float(input("Digite sua altura em metros: "))
p = float(input("Digite seu peso em kg: "))
imc=p/(a)**2
print("Seu IMC é de {:.2f} =".format(imc), end=" ")
if imc<18.5:
    print("ABAIXO DO PESO")
elif imc>18.5 and imc<25:
    print("PESO IDEAL")
elif imc>25 and imc<30:
    print("SOBREPESO")
elif imc>30 and imc<40:
    print("OBESIDADE")
elif imc>40:
    print("OBESIDADE MÓRBIDA")
