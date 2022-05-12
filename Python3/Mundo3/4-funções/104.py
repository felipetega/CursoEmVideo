'''Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)'''
def leiaInt(n):
  if n.isnumeric():
    print(n)
  else:
    print("Valor negado")

n=input("Digite um valor numérico: ")
leiaInt(n)