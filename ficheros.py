"""
#ARCHIVOS PLANOS
#1 READLINE()
from io import open
fichero= open('fichero.txt','r')
texto = fichero.readlines()
fichero.close()
print(texto)
#2 WITH DE MANERA AUTOMATICA, 
with open ("fichero.txt","r") as fichero:
    for linea in fichero:
        print(linea)

#APPEND
fichero = open('fichero.txt', "a")
fichero.write('\n otra linea')
fichero.close()

#METODO SEEK(), PUNTERO EN EL FICHERO no retorna nada
fichero = open("fichero.txt","r")
fichero.seek(0) #puntero al inicio
fichero.seek(10) # leemos los 10 caracteres
"""
"""
texto = "una linea de texto \notra linea con texto"
fichero=open('fichero.xml','w')
fichero.write(texto)
fichero.close()
"""

fichero = open("texto.txt","w")
texto = "hola"
fichero.write(texto)
fichero.close