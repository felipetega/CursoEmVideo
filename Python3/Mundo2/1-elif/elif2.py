from msilib.schema import Binary
from xmlrpc.client import _binary


x = int(input("Digite um número inteiro: "))
y = str(input("Escolha a base de conversão, entre: binário, octal e hexadecimal: ")).strip().lower()
if y == "binario" or "binário":
    print("O binário de 'x' é: {}".format(x.binary()))


