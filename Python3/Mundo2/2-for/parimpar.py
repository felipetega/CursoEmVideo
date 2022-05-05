from multiprocessing.pool import IMapIterator


par = 0
impar = 0
for x in range(0,6):
    x = int(input("Número Inteiro: "))
    if x % 2 == 0:
        par = par + x
    if x % 2 == 1:
        impar = impar + x
print("A soma dos números pares é de {}".format(par))
print("A soma dos números impares é de {}".format(impar))
