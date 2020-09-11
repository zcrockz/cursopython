
while True:

    print("\nBienvenido")
    opcion = int(input("Que quieres hacer? \n 1.- Saludar\n 2.- Sumar dos numeros\n 3.- Salir\n\t "))
    
    if opcion == 1:
        print("Hola como estas\n\t")
    elif opcion == 2:
        num_1 = int(input("Ingresa el primer numero: \n\t"))
        num_2 = int(input("Ingresa el segundo numero: \n\t"))
        total = num_1 + num_2
        print("la suma entre {} y {} ".format(num_1, num_2), "Es: ", total) 
    elif opcion == 3:
        print("Adios")
        break
    else:
        print("Comando erroneo\t") 
        



     