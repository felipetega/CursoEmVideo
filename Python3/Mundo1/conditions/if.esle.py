n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = (n1+n2)/2
if (n3 >= 6):
    print("Parabens, você passou com média {}".format(n3))
else:
    print("Que pena, você não passou na matéria, média {}".format(n3))
