vel = int(input("Digite a velocidade do carro em km/h: "))
multa = (vel-120) * 7 
if vel < 120:
    print("Voce está dentro do limite de velocidade, faltam {} km/h para a velocidade máxima permitida".format(120-vel))
else:
    print("Você ultrapassou o limite de velocidade, vai ser multado em ${}".format(multa))
