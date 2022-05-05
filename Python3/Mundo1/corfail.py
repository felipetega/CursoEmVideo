from distutils import core


nome = 'Felipe'
espaço = ' '
cores = {'azul':'\033[34m',
        'neutro':'\033[97m'}

print("Salve Salve, {}{}{}".format(nome, cores['azul'], espaço, cores['neutro']))
