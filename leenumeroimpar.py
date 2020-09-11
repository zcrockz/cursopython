#CONTROL DE FLUJO
##2) LEE NUMERO IMPAR POR TECLADO

while (True):

    lectura = int(input("Ingresar un Numero Impar: ")) 
    resultado = lectura % 2
    if resultado == 1:
        print("Numero impar")
        break
    else:
        print("""No es un numero impar
        Vuelve a intentarlo """)

