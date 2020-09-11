fichero= open('personas.txt','r')
lineas = fichero.readlines()
fichero.close()
lista=[]

for linea in lineas:
    campos = linea.replace("\n","").split(";")
    print(campos)
    dic = {"id":campos[0], "nombre":campos[1], "apellido":campos[2], "fecha":campos[3]}
    #print(dic)
    lista.append(dic)

for elemento in lista:
    print("El dic: {} {} {} {} ".format(elemento["id"], elemento["nombre"], elemento["apellido"],elemento["fecha"]))
