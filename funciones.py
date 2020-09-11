def intro():
    print("Ingrese los datos para calcular el area de triangulo ")
    base =int(input("Ingresar la base: "))
    altura=int(input("Ingresar la altura: "))
    datos = calcular(base,altura)
    imprimir(datos)

def calcular(a,b):
    return a * b


def imprimir(datos):
    print("El valor es ",datos)

intro()