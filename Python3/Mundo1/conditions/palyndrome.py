nome = str(input("Digite seu nome: "))
i = len(nome)
palindrome = ""
while i > 0:
    palindrome += nome[i-1]
    i -= 1
if nome == palindrome:
  print("É PALÍNDROMO")
else:
  print("NÃO É PALÍNDROMO")
