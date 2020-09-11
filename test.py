try:
    seleccion =input("""\nMenu
    1.Suma de dos numeros
    2. Resta de dos numeros
    3. Multiplicacion de los dos numeros
    seleccion: 
    """)

    if seleccion == 1:
       num1 = int(input("Ingresa primer numero: "))
       num2 = int(input("Ingresa segundo numero: "))
       resultado = num1 + num2
       print("\nEl valor de la suma es {}".format(resultado))

except Exception as e:
        print("\033[1;33m"+"ha ocurrido un error " +'\033[0;m', type(e).__name__)

