"""
texto = "un dia que el viento soplaba con fuerza # mira como se mueve aquella banderola -dijo un monje# lo que se mueve es el viento -respondio otro monje# ni las banderolas ni el viento, lo que se mueve son vuestras mentes -dijo el maestro"
list1=[]
list2=[]
list3=[]

lineas = texto.split("#")
print(lineas)

for n, datos in enumerate(lineas):

"""    





def modificar(lis):
    lista = list(set(lis)) #elimina los duplicados
    print(lista)

    lista.sort(reverse=True) #los ordena en orden ascendente
    #print("Lista ordenada {}".format(lista))
    print(lista)
    listapares=[]

    for n in lista:
        #print(n)
        
        if n%2 == 0:
            listapares.append(n)
            print(n)
    
    print(lista)

    suma = sum(listapares) #40
    listapares.insert(0,suma)
    #print("Lista mas la suma al inicio {}".format(lista))
    return listapares       
if __name__ == "__main__":
    lista = [29,-5,-12,17,5,24,5,12,23,16,12,5,-12,17]
    lista_nueva = modificar(lista)
    print(lista_nueva)

