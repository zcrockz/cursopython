
#CONTROL DE FLUJOS
#1) REALIZAR UN PROGRAMA  QUE LEA DOS NUMEROS POR TECLADO Y PERMITA ELEGIR ENTRE 3 OPCIONES EN UN MENU

while(True):
    
    try:     
        seleccion = int(input("""\nMenu)
        1.Suma de dos numeros
        2. Resta de dos numeros
        3. Multiplicacion de los dos numeros
        seleccion: 
        """))

        if seleccion == 1:
            num1 = int(input("Ingresa primer numero: "))
            num2 = int(input("Ingresa segundo numero: "))
            resultado = num1 + num2
            print("\nEl valor de la suma es {}".format(resultado))

        if seleccion == 2:
            num1 = int(input("Ingresa primer numero: "))
            num2 = int(input("Ingresa segundo numero: "))
            resultado = num1 - num2
            print("\nEl valor de la resta es {}".format(resultado))

        if seleccion == 3:
            num1 = int(input("Ingresa primer numero: "))
            num2 = int(input("Ingresa segundo numero: "))
            resultado = num1 * num2
            print("\nEl valor de la Multiplicacion es {}".format(resultado))
        if seleccion >3:
            print("\033[1;33m"+"El numero no existe" +'\033[0;m')
    

    except ValueError:
        print("\033[1;33m"+"Solo Numeros" +'\033[0;m')
    




