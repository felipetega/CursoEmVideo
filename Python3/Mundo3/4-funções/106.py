'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
from time import sleep


def titulo(a, cor):
    print(f'{cor}~'*(len(a)+4))
    print(f'  {a}  ')
    print('~' * (len(a) + 4))


def leia(pergunta):
    global x
    x = input(pergunta)


def ajuda():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', '\033[1;97;42m')
        leia('\033[mFunção ou Biblioteca > ')
        if x == 'fim':
            titulo('ATE LOGO!', '\033[1;97;41m')
            sleep(2)
            break
        titulo(f"Acessando o manual do comando '{x}'", '\033[1;97;44m')
        print('\033[;30;107m')
        help(x)


# Programa Principal
x = ()
ajuda()