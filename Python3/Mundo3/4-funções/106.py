'''Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
def programa(*a):
    '''
    Multiplica todos os valores fornecidos e diz o resultado
    '''
    c = 0
    x = 1
    while c < len(a):
        x *= a[c]
        c += 1
    print(f"O produto de todos os valores foi de {x}")


programa(1, 3, 5)
