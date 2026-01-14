# Resolucion de ejercicios Unit 7
# Solution of exercises Unit 7

# En el siguiente ejercicio se solicitara calcular el area y el permetro de un rectangulo
# para ello se debera solicitar al usuario que ingrese el valor de la base y la altura del rectangulo
# Finalmente se debera imprimir en la terminal el area y el perimetro del rectangulo

# In the following exercise, you will be asked to calculate the area and perimeter of a rectangle
# for this, the user must be asked to enter the value of the base and height of the rectangle
# Finally, the area and perimeter of the rectangle must be printed on the terminal

base = float(input("Ingresa el valor de la base del rectangulo: "))
altura = float(input("Ingresa el valor de la altura del rectangulo: "))

area = base * altura
perimetro = 2 * (base + altura)
print("El area del rectangulo es:", area)
print("El perimetro del rectangulo es:", perimetro)