import os
from time import sleep as tiempo


def crear_archivo():
    print("Crear un archivo\n Ejemplo: nombre.txt")
    archivo = input("Nombre del archivo: ")   
    nombre = open(archivo,'w')     
    nombre.close()
    return nombre   

def leer_archivo(nombre):
    
    if  os.path.isfile(nombre):   
        with open (nombre,"r") as fichero:
            for linea in fichero:
                print("Resultado: ")
                print(linea)
    else:
        print("no existe el archivo con nombre {}".format(nombre))


def leer_todas_lineas():
    fichero= open('hola.txt','r')
    lineas = fichero.readlines()
    fichero.close()
    print(lineas)
    for n,m in enumerate(lineas):
        lineas = m.replace("\n","").split(";")
        print(m)

def leer_linea_linea(nombre):
    fichero= open("Hola.txt",'r')
    lineas = fichero.readlines()
    fichero.close()
    print(lineas)
    for linea in lineas:
        campos = linea.replace("\n","")
        print(campos)

#    fichero.seek(len(linea))

def archivo_existe(nombre):
    if  os.path.isfile(nombre):  
        print("Abriendo...")
        tiempo(2)
    else:
        print("no existe el archivo con nombre {}".format(nombre))    

def menu():

    print("""EDITAR ARCHIVOS\n
    Menu:\n
    1.- Crear Archivo
    2.- Abrir archivo
    3.- Leer linea a linea""")
    
    seleccion = int(input("Seleccione: "))
    if seleccion == 1:#crear archivo
        nombre = crear_archivo()
        print(nombre)
    if seleccion == 2:#Buscar el archivo por nombre        
        nombre = input('\tIngrese el nombre del archivo: ')
        #archivo_existe(nombre)
        print("\tSeleccione lo que desea hacer")
        print("\t1.- Leer todo el archivo")
        print("\t2.- Leer linea a linea")
        seleccion = int(input(("\t\tEscoja: ")))
        if seleccion == 1:
            leer_archivo(nombre)
        if seleccion ==2:
            leer_linea_linea(nombre)
        
    
if __name__ == "__main__":
    menu()
    #crear_archivo()
    #leer_archivo()
    #leer_todas_lineas()
    #leer_linea_linea()







