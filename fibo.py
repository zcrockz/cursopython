from matplotlib import pyplot as plt

def graficofibo(listax,listay): #argumentos
    #eje_y = range(0,20,3)
    #print(list(eje_y))
    plt.grid(linestyle='--',linewidth=2)
    plt.xlabel("Valor")
    plt.ylabel("Fibonacci")
    plt.title("CALCULO DE UN NUMERO FIBONACI")
    plt.xscale('linear')
    #plt.plot(x,y1, marker='o', markersize=10, markerfacecolor="green", markeredgewidth= "1", markeredgecolor = "red", lw=4)
    plt.plot(listax,listay, marker='o', markersize=10, markerfacecolor="green", markeredgewidth= "1", markeredgecolor = "red", lw=4)
    plt.legend(["Curva de Linea FIBO"])
    plt.show()

#FUNCION FIBO
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":

    numero = int(input("Ingrese el numero:  "))
    x = list(range(0,numero+1))   
    #BENDITO FOR
    #for numero in range(numero):
    #    print(fib(numero))
    #BENDITA LISTA
    print("Es el numero",fib(numero))
    y = [fib(numero) for numero in range(numero+1)]
    print(y)
    print(x)
    graficofibo(x,y) #parametros