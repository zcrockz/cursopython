lista_1= []
lista_1 = list(input("Ingrese una Lista: \n\t "))
print(lista_1)

for n in lista_1:
    #print(n)
    impar = int(n) % 2
    print(impar)
    if impar == 1:
        n = n*5
        #print(n)
    else: 
        n = n*10
        #print(n)

