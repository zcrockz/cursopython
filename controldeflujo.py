#5) Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo:
numeros = [1, 3, 6, 9]

"""
while True:
    valor = int(input("Ingrese un numero entre 0 y 9: "))
    if valor >= 0 and valor <= 9:
        for m in numeros:
            if m == valor:
                print("Ese valor ya existe")
    else:
        print("Valor fuera de rango")

"""

#6) Utilizando la función range() y la conversión a listas genera las siguientes listas dinámicamente:
#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
#Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]


todos_numeros = list(range(0,11))
print("todos los numeros\n", todos_numeros)

todos_numeros = list(range(-10,0))
print("todos los numeros del -10 al 0\n", todos_numeros)

todos_numeros = list(range(0,22,2))
print("todos los numeros pares del 0 al 20\n", todos_numeros)

lista =[]
todos_numeros = list(range(-20,0,1))
#print(todos_numeros)
for n,m in enumerate(todos_numeros):
    if n%2 != 0:
        lista.append(m)
print("todos los numeros impares entre -20 y 0\n", lista)     


todos_numeros = list(range(0,55,5))
print("todos los numeros multiples de 5  del 0 al 50\n", todos_numeros)

#7) Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetise ningún elemento en la nueva lista:
list1 = [6,7,8,21,10] 
list2 = [6,7,8,9,10]
lista3 = []
for n,m in enumerate(list1):
    lista3.append(m)
for n,m in enumerate(list2):
    lista3.append(m)
lista3 = list(set(lista3)) #elimina los duplicados
print("Suma 2 listas y no se replica\n ",lista3)





