# EJERCICIO 1
"""
print('Ingresar dos numeros')
numero1= int(input("Ingresar primer numero: "))
numero2= int(input("Ingresar segundo numero: "))

if numero1==numero2:
    print("los dos numeros son iguales")
else:
    print('No son iguales')

if numero1 != numero2:
    print('numeros diferentes')

if numero1 >= numero2:
    print('primer numero es mayor que el segundo')

if numero1 <= numero2:
    print('el segundo numero es mayor que el primero')

"""

#EJERCICIO 2
"""
texto = str(input('Ingrese un texto:'))
numero = len(texto)
print(numero)
if numero >= 3:
    print(True)
else:
    print(False)

if numero < 10:
    print(True)
else:
    print(False)
 
"""

# EJERCICIO 3

variable_magico = int(12345679)
numero =int(input("Ingrese un numero entre 1 y 9: "))
numero*=9
variable_magico*=numero
print(variable_magico)
