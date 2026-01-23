# Ejercicio: crea un algoritmo que detecte cuál es el número mayor entre dos números

"""
Instrucciones de tareas:
Solicitar al usuario dos valores, y determinar cuál número es el mayor
Solicitar al usuario dos valores
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos números ( la salida debe ser idéntica a que sigue):
Proporciona el numero1 
Proporciona el numero2
El número mayor es :<Numero_mayor>
"""
# Solución 

# Exercise: Create an algorithm that detects which is the larger of two numbers.

"""
Task instructions:
Ask the user for two values ​​and determine which number is larger.
Ask the user for two values:
number1 (int)
number2 (int)
Print the larger of the two numbers (the output should be identical to the following):
Enter number1
Enter number2
The larger number is: <Largest_number>
"""

# Solution

numero1 = int(input('Proporciona el numero 1: '))
numero2 = int(input('Proporciona el numero 2: '))

if numero1 > numero2:
    print("Numero 1 es mayor")

elif numero1 == numero2:
    print("Los dos numeros son iguales")

else: 
    print("Numero 2 es mayor")
