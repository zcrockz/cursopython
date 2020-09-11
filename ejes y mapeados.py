"""
import matplotlib.pyplot as plt
#%matplotlib inline  # con esto solo es necesario imprimir y omites el show()

gastos = [50,120,80,95]
meses = ["enero", "febrero", "marzo", "Abril"]
mapeo = range(len(meses))

plt.plot(gastos)
plt.xticks(mapeo,meses)
print(list(mapeo))
plt.show() # si no pones la clausula debes escribir .show()


#eje x y Y

x = [0,5,10,15]
y = gastos
plt.plot(x,y) # METODO QUE REPRESENTA DATOS EN PLANO CARTESIANO
plt.show()

#Grafico invertido

plt.plot(y,x)
plt.show()

"""



#COMPRENSION DE LISTAS
#1
#metodo tradicional
lista = []
for letra in "casa":
    lista.append(letra)
#print(lista)
#con compresion de listas
lista = [letra for letra in "casa"]
print(lista)
#2
#metodo tradicional
lista =[]
for numero in range (0,11):
    lista.append(numero**2)
pares =[]
for numero in lista:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#compresion de listas

lista = [numero for numero in [numero**2 for numero in range(0,11)] if numero % 2 == 0]
print(lista)



#LIMITES xlim, ylim
import matplotlib.pyplot as plt

x = range(1,11) # numero del 1 al 10
y = [n**2 for n in x] # potencias de 2 del 1 al 10
print(y)
plt.plot(x,y)
#plt.xlim(-10,20) # zoom hacia afuera
plt.xlim(len(x)-5, len(x)) # zoom hacia dentro
plt.ylim(0,200)
plt.show()


#titulo y etiquetas

x = range(1,11)
y = [n**2 for n in x]
plt.plot(x,y)
plt.title("nombre")
plt.xlabel("eje x")
plt.ylabel("eje y")

#como a;adir de una al plot el label de leyenda

plt.plot(x,y, label ="a la 2")
plt.title("potencias")
plt.xlabel("numero")
plt.ylabel("resultado")
plt.legend() # con el parametro lo podemos establecer una posiicon del 0 al 10 (0 es por defecto, 10 es el centro)

