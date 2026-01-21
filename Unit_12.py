# Ejercicio: crea un algoritmo que detecte cual es el numero mayor entre dos numeros

"""
Instrucciones de tareas:
Solicitar al usuario dos vaolores, y determinar cual numero es el mayor
Solicitar al usuario dos valores
numero1 (int)
numero2 (int)
Se debe imprimir el mayor de los dos numeros ( la salida debe ser identica a a que sigue):
Proporciona el numero1 
Proporciona el numero2
El numeroa mayor es :<Numero_mayor>
"""
# Solucion 

numero1 = int(input('Proporciona el numero 1: '))
numero2 = int(input('Proporciona el numero 2: '))

if numero1 > numero2:
    print("Numero 1 es mayor")

elif numero1 == numero2:
    print("Los dos numeros son iguales")

else: 
    print("Numero 2 es mayor")
