pessoa=[]
listaPessoas=[]
p=int(input("Quantas pessoas irão ser registradas? "))
c=0
while c<p:
    nome=str(input("Nome: "))
    pessoa+=nome,
    idade=int(input("Idade: "))
    pessoa+=idade,
    print(pessoa)
    listaPessoas.append(pessoa)
    pessoa=[]
    c+=1
print(listaPessoas)
