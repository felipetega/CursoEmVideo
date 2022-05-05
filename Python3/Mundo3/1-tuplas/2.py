'''Crie um programa que tenha uma dupla totalmente preenchida
com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado (entre 0 e 20)
e mostrá-lo por extenso.'''
num = ("zero","um","dois","três","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","treze","quatorze","quinze","dezesseis","dezessete","dezoito","dezenove","vinte")
x = int(input("Digite um número entre 0 e 20: "))
while x not in range(0,21):
    x = int(input("Tente novamente. Digite um número entre 0 e 20: "))
print(f"Você digitou o número {num[x]}")
