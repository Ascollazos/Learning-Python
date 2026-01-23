# Ejercicio para convertir un número entregado por el usuario a texto
# Exercise to convert a number entered by the user to text

# Creamos una variable y la definimos como entero
# We create a variable and define it as an integer
numero = int(input("Proporciona un numero entero entre 1 y 3: "))
if numero == 1:                 # Agregamos varios condicionales dependiendo de los números que vamos a convertir
    numeroTexto = "Numero uno"  # Cambiamos el valor de las variables a texto
elif numero == 2:
    numeroTexto = "Numero dos"  # add several conditional statements depending on the numbers we're going to convert.
elif numero == 3:               # change the variable values ​​to text.
    numeroTexto = "Numero tres"
else:                           # Agregamos un condicional else para los valores fuera de rango
                                # We add an else conditional for out-of-range values
    numeroTexto = "Valor fuera de rango"
print(f'El numero proporcionado: {numero} - {numeroTexto}') 
