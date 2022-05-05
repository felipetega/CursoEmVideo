from cgi import print_directory
from time import sleep
from random import randint

x = int(input("\033[36mEscolha entre 1-pedra, 2-papel e 3-tesoura: "))

print("JO")
sleep (1)
print("KEN")
sleep(1)
print("PO")
sleep(1)

y = randint(1,3)

if x == 1:
    print("\033[33mJOGADOR 1 ESCOLHEU: PEDRA",end=" \033[30m- ")
if x == 2:
    print("\033[33mJOGADOR 1 ESCOLHEU: PAPEL",end=" - ")
if x == 3:
    print("\033[33mJOGADOR 1 ESCOLHEU: TESOURA",end=" - ")

if y == 1:
    print("\033[35mJOGADOR 2 ESCOLHEU: PEDRA")
if y == 2:
    print("\033[35mJOGADOR 2 ESCOLHEU: PAPEL")
if y == 3:
    print("\033[35mJOGADOR 2 ESCOLHEU: TESOURA")

if x==1 and y==3 or x==2 and y==1 or x==3 and y==2:
    print("\033[32mVOCE VENCEU")
if x==1 and y==2 or x==2 and y==3 or x==3 and y==1:
    print("\033[31mVOCE PERDEU")
if x==y:
    print("\033[34mEMPATOU")
