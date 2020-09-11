
#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

def primergrafico(listax1,y1,listax2,y2, listax3,y3):
    
    #primero
    
    plt.subplot(1,3,1) # tabla 1x3 celda 1
    plt.plot(listax1,y1,marker='o', markersize=10, markerfacecolor="green", markeredgewidth= "1", markeredgecolor = "red", lw=4)
    plt.title("Num1")

    #segundo
    #plt.title("Fig2")
    plt.subplot(1,3,2)
    plt.plot(listax2,y2,"b-+", marker='*', markersize=10, markerfacecolor="black", markeredgewidth= "1", markeredgecolor = "red", lw=4)
    plt.title("Num2")

    #tercero
    
    plt.subplot(1,3,3)
    plt.plot(listax3,y3,"g-.",marker='o', markersize=10, markerfacecolor="red", markeredgewidth= "0.2", markeredgecolor = "red", lw=4)
    plt.title("Num3")
    #presenta la imagen
    plt.show()


def factorial_1 (n1,n2,n3):
    listax1 =[]
    listax2 =[]
    listax3 =[]
    y1=[]
    y2=[]
    y3=[]
    #lista=[n1,n2,n3]
    #mayor = max(lista)
    #print(mayor)
    numero = list(range(1,n1+1))
    listax1 = numero
    print("eje x: ",listax1)
    #for x in n:
    fac=1
    for y in range(1,n1+1):
        fac=fac*y
        y1.append(fac)
    print ("eje y1: ",y1)
    #primergrafico(listax,listay)
    
    numero = list(range(1,n2+1))
    listax2 = numero
    print("eje x: ",listax2)
    fac=1
    for y in range(1,n2+1):
        fac=fac*y
        y2.append(fac)
    print ("eje y2: ",y2)

    numero = list(range(1,n3+1))
    listax3 = numero
    print("eje x: ",listax3)
    fac=1
    for y in range(1,n3+1):
        fac=fac*y
        y3.append(fac)
    print ("eje y3: ",y3)

    primergrafico(listax1,y1,listax2,y2,listax3,y3)

#factorial()
n1 = int(input("INgrese Numero 1: "))
n2 = int(input("INgrese Numero 2: "))
n3 = int(input("INgrese Numero 3: "))
factorial_1(n1,n2,n3)




