import matplotlib.pyplot as plt
from random import sample

x = range(1,11)
y0 = [n**0 for n in x]
print(y0)
y1 = [n**1 for n in x]
y2 = [n**2 for n in x]
#y3 = [n**5 for n in x]

plt.plot(x, y0, label = "A la 0")
plt.plot(x, y1, label = "A la 1")
plt.plot(x, y2, label = "A la 2")
#plt.plot(x, y3, label = "A la 3")

plt.title("Potencia")
plt.xlabel("Numero")
plt.ylabel("resultado")
plt.legend()
plt.show()

# estilos de linea

x = range(1,11)
y1 = sample (range(-10,10), len(x))
test = sample(range(6),2)
print(test)
print(y1)
y2 = [n+5 for n in y1]
y3 = [n-5 for n in y1]

plt.plot(x,y1, ls="-", lw=2, color="#ffb90f", alpha=0.25, label="n")
plt.plot(x,y2,"b--", lw=2,label="n +5")
plt.plot(x,y3,"g-.", lw=2,label="n - 5")

plt.legend()
plt.show()