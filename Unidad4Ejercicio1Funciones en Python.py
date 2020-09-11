import math

def area_circulo(radio):
    area = (radio*radio)*math.pi
    return area 

def area_rectangulo(base, altura):
    resultado = base*altura 
    return resultado


def relacion (num1,num2):
    if num1 > num2:
        return 1
    elif  num1 < num2:
        return -1
    elif num1 == num2:
        return 0


def intermedio(num1,num2):
    resultado = (num1+num2)/2
    return resultado


def recortar (num_recortar,limite_inferior,limite_superior):

    if num_recortar < limite_inferior:
        return limite_inferior
    elif num_recortar > limite_superior:
        return limite_superior
    elif  num_recortar > limite_inferior or num_recortar <limite_superior:
        return num_recortar


def separar(lista):
    pares =[]
    impares =[]
    for m in lista:
        if m % 2 == 0:
            pares.append(m)
        elif m % 2 == 1:
            impares.append(m)
    pares.sort()
    impares.sort()
    print("Los pares son: ",pares)
    print("Los impares son: ",impares)
        

if __name__ == "__main__":
    radio = int(5)
    valor = area_circulo(radio)
    print("El area de un circulo de radio {} es: {} ".format(radio,valor))

    base = 15
    altura = 10
    resultado = area_rectangulo(base,altura)
    print("El area del rectangulo entre {} y {} es {}".format(base,altura,resultado))

    result = relacion(5,5)
    print(result)

    valor_intermedio = intermedio(-12,24)
    print("El valor intermedio entre -12 y 24 es: {} ".format(valor_intermedio))

    valor_recortar = recortar(15,0,10)
    #print(valor_recortar)

    lista = [-12, 84, 13, 20, -33, 101, 9]
    print("Su lista inicial es :",lista)
    resultado = separar(lista)


