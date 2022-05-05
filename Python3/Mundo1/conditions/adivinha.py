from time import sleep
from random import randint
a = randint(1,3)

x = int(input("Pensei em um número de 1 a 3... Adivinhe qual é: "))
print("\033[35mPROCESSANDO...")
sleep(3)

if x == a:
    print("\033[32mACERTO MIZARAVI\033[0m")
else:
    print("\033[31mPERDEU PLAYBOY, o número q eu pensei foi {}\033[0m".format(a))
