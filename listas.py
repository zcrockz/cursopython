#Lista = []

#valor = ("Ingrese entero flotante, string, lista")

#valor = int(input("Ingresa un dato entero: "))
#Lista. append(valor)

#valor_1 = float(input("Ingresa un valor flotante: "))
#Lista.append(valor_1)

#valor_2 = str(input("Ingresar un valor String: "))
#Lista.append(valor_2)

#valor_3 = list(input("Ingresar una lista: "))
#Lista.append(valor_3)

#print("El valor de su lista es {}".format(Lista))

#
#Lista = []
#Lista = list(input("Ingresar una lista: "))
#print("Su lista es: {}".format(Lista))
#valor_2 = int(input("Que indice de su lista desea cambiar: "))
#cambio = int(input("Ingresar el valor a cambiar:  "))
#Lista[valor_2] = cambio
#print(" Su nueva lista es: {}".format(Lista))


Lista_1 = []
Lista_2 = []

print("Ingresar 2 listas")
Lista_1 = list(input("Lista 1 Enteros: "))
print(Lista_1)
Lista_2 = list(input("Lista 2 String: "))
print(Lista_2)

valor_append = input('Ingresar valor para append en lista 1: ')
Lista_1.append(valor_append)
print(Lista_1)

valor_insert = input('Ingresar valor para insert en lista 1 en posicion 2: ')
Lista_1.insert(2, valor_insert)
print(Lista_1)

valor_pop = int(input('Ingresar valor de index para pop : '))
Lista_1.pop(valor_pop)
print(Lista_1)

valor_remove = input('Ingresar para remover')
Lista_1.remove(valor_remove)
print(Lista_1)