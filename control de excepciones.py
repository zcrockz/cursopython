
"""
while True:

    try:
        n = input("Introduce un numero: ")
        5/n
    except Exception as e:
        print("ha ocurrido un error ", type(e).__name__)
"""
"""
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("error no se permite un valor nulo")
    except ValueError:
        print("Error no se permite un valor nulo (desde la excepcion)")

mi_funcion()


while(True):
    try:
        n = float(input("Introduce un numero: "))
        m=4
        print("{}/{} = {}".format(n,m,n/m))
    except:
        print("ha ocurrido un error")
    else:
        print("todo fucionando correctamente")
        break
    finally:

        print("fin de la interaccion ")
"""


while(True):

    try:    
        numero = int(input("Ingrese un numero: "))
        resultado = 10/numero
        print(resultado)

    except Exception as e:
        print("ha ocurrido un error ", type(e).__name__)
        #finally:
            
            


"""
while (True):
    lista = []   
    lista = list(input('Ingrese una lista: '))
    contador =0
    print(lista)


    for n,m in enumerate(lista):
        contador= contador+1
        print("\x1b[1;33m"+"{}.-Valor de indice: {} y valor del indice {}".format(contador,n,m))

    try: 
        seleccion = int(input(("cual deseas sacar?: ")))
        valor = lista[seleccion-1]
        print("valor es: {}".format(valor))
    except IndexError:
            print("No existe el indice ")
    except ValueError:
            print("Valor erroneo")
    #except TypeError:
    #        print("Tipo de error")
    except Exception as e:
        print("ha ocurrido un error ", type(e).__name__)
    


"""









