from datetime import date

nas = int(input("Digite o ano do seu nascimento: "))
ano=date.today().year
idade=ano-nas
alis=idade-18
if idade==18:
    print("Você deve se alistar esse ano")
elif idade<18:
    print("Você deverá se alistar daqui {} ano(s)".format(18-idade))
elif idade>18:
    print("Seu alistamento foi {} anos atrás".format(idade-18))
