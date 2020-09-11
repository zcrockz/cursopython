import matplotlib.pyplot as plt

from random import sample

x = range(1,11)
y1 = sample(range(50), len(x))
y2 = sample(range(50), len(x))

plt.plot(x,y1, marker='o', markersize=10, markerfacecolor="green", markeredgewidth= "1", markeredgecolor = "red", lw=4)
plt.plot(x,y2, marker='*', markersize=15, markerfacecolor="red", markeredgewidth= "1", markeredgecolor = "black", lw=4) #argumentos
plt.show()

#SUBGRAFICOS

x = range (1,11)
plt.subplot(1,2,1) # tabla 1x2 celda 1
y1= sample(range(20),10)
plt.plot(x,y2,"b")

plt.subplot(1,2,2) # tabla 1x2, celda 2   //los argmentos de subplot (1 fila y 2 columnas, 3 la posicion)
y2= y1[::-1] #lista invertida de y1 con slicing
print(y2)
plt.plot(x,y2,"g")
plt.show()

#Figuras

fig = plt.figure()
#limites del rectangulo (l,b,w,h)
rect = (0,0,1.0,1.0)
axes  = fig.add_axes(rect)

x = range (1,11)
y = sample(range(20), len(x))
axes.plot(x,y)

axes.set_xlabel("eje x")
axes.set_ylabel("eje y")
axes.set_title("titulo")

plt.show()

#SUBGRAFICOS EN FIGURAS
#DOS OPCIONES EN POSICIONAMIENTO LIBRE Y POSICIONAMIENTO EN CUADRICULA
fig = plt.figure()

x= range(1,11)
y1 = sample(range(20),len(x))
y2 = sample(range(20),len(x))


rect1 = (0,0,2,1)
axes1 = fig.add_axes(rect1)
axes1.plot(x,y1)
axes1.set_title("Grafico Grande")
plt.show()


#rect2 = (0.1,0.2,0.1,0.1)
#axes2 = fig.add_axes(rect2)
#axes2.plot(x,y2)
#axes2.set_title("Grafico pequeno")
#plt.show()


# POSICIONAMIENTO EN CUADRICULA

fig, axes = plt.subplots(nrows=2, ncols=2)

x = range()