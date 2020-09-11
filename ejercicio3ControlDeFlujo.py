#3)SUMA TODOS LOS NUMEROS ENTEROS DESDE EL 0 AL 100
"""
lista=list(range(0,100,2))
print(sum(lista))
"""
#4)REALIZA UN PROGRAMA QUE PIDA AL USUARIO CUANTOS NUMEROS QUIERE INTRODUCIR. LUEGO LEE TODOS LOS NUMEROS Y REALIZA UNA MEDIA ARITMETICA

cantidadNumeros = int(input("Ingresa cuantos numeros: "))
lista = list(range(0,cantidadNumeros))
#print(lista)
for n,m in enumerate(lista):
    lista[n] = int(input("Ingrese el Valor: "))
    #print(lista)
contador =0
for n in lista:
    contador = contador + 1
    print("numero {}: {}".format(contador,n))
    #print(n)

#print(lista)    
resultado=sum(lista)/cantidadNumeros
print("La media es: {} ".format(resultado))