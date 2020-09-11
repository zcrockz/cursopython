import pickle

#guardar ficheros en binario
"""

lista = [1,2,3,4,'\n']
fichero = open("lista.cz","wb") # cualquier extencion
pickle.dump(lista,fichero)
fichero.close()
"""

#recupera estructura de fichero binario
fichero = open ("lista.cz", "rb")

lista_fichero = pickle.load(fichero)
print(lista_fichero)
fichero.close()
