while True:
  try:
    i=int(input("Digite um número inteiro: "))
  except ValueError:
    print("Digite um número inteiro válido")
  else:
    break
while True:
  try:
    r=float(input("Digite um número real: "))
  except ValueError:
    print("Digite um número real válido")
  else:
    break
print(f"Você digitou os números {i} e {r}")