
#LISTAS

matriz = [[1,1,1,3], [2,2,2,7],[3,3,3,9], [4,4,4,13]] 
lista = []
#CON EL FOR LE HICE 
contador = 0
for n,m in enumerate(matriz):
    matriz = m
    valor = sum(matriz[0:3])
    matriz[3]=valor
    print(matriz)

#SIN EL FOR
"""

pos0=matriz[0]
pos0[3]=sum(pos0[0:3])
#print(pos0)

pos1=matriz[1]
pos1[3]=sum(pos1[0:3])
#print(pos1)

pos2=matriz[2]
pos2[3]=sum(pos2[0:3])
#print(pos2)

pos3=matriz[3]
pos3[3]=sum(pos3[0:3])
#print(pos3)

matriz = [pos1,pos2,pos3]
print(matriz)"""

#CADENAS

cadena = "zereP nauJ, 01"
lista = []
lista = cadena[::-1]
numero=lista[0:3] 
coma = lista[3]
cadena2 = lista[4:14]
cadena = cadena2 + coma + numero 
print(cadena)


