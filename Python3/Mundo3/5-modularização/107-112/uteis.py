def dobro(x):
  res=x*2
  return res


def metade(x):
  res=x/2
  return res


def aumento(x):
  res=x*1.1
  return res


def reducao(x):
  res=x*0.9
  return res


def moeda(x=0):
  return f'R${x:.2f}'.replace('.', ',')