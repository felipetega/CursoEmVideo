dis = int(input("Qual a distância até o seu destino em km? "))
pas1 = 0.50*dis
pas2 = (200*0.50)+((dis-200)*0.45)
if dis < 200 :
    print("O preço da passagem ficou ${}".format(pas1))
else:
    print("O preço da passagem ficou ${}".format(pas2))
