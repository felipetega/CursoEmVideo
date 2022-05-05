'''Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
Não ta mudando d opção'''

from random import randint
print('Par ou Ímpar!')
vitoria = 0
escolha = 0
while True:
    while escolha != 1 and escolha != 2:
        escolha = int(input('1 - Par \n2 - Ímpar \n'))
        if escolha != 1 and escolha != 2:
            print('Opção Inválida!')
    jogador = int(input('Digite um número de 0 a 10: '))
    pc = randint(0, 10)
    if escolha == 1:
        print(f'Jogador escolheu: {jogador} e o Computador escolheu: {pc} ')
        if (jogador + pc) % 2 == 0:
            print(f'{jogador}+{pc}:{jogador+pc} , Jogador vence!')
            escolha = 0
        else:
            print(f'{jogador}+{pc}:{jogador+pc} , Computador vence!')
            break
    if escolha == 2:
        print(f'Jogador escolheu: {jogador} e o Computador escolheu: {pc} ')
        if (jogador + pc) % 2 == 0:
            print(f'{jogador}+{pc}:{jogador+pc} , Computador vence!')
            break
        else:
            print(f'{jogador}+{pc}:{jogador+pc} , Jogador vence!')
            escolha = 0
    vitoria += 1
print(f'Voce teve um total de {vitoria} vitórias.')