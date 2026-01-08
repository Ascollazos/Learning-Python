#Leccion 4: Operaciones sencillas
#Lesson 4: Simple Operations

Num_sum_1 = 2
Num_sum_2 = 2

sum_result = Num_sum_1 + Num_sum_2

print(sum_result)

Num_rest_1 = 2.5
Num_rest_2 = 1

rest_result = Num_rest_1 - Num_rest_2
print(rest_result)

Num_mult_1 = 2
Num_mult_2 = 3.14

mult_result = Num_mult_1 * Num_mult_2
print(mult_result)

Num_Div_1 = 10
Num_Div_2 = 2

div_result = Num_Div_1 / Num_Div_2
print(div_result)

#Leccion 5: Direccion de memoria y variables
#Lesson 5: Memory addressing and variables

Y = 10                      
id(Y)                   
print(id(Y))

# La variable "Y" se le asigna un valor 10, pero donde sabemos
# que se guarda el valor de la variable los valores se guardan
# Con esta funcion puedes ver el valor en la memoria que tene la variable
# Esto se usa para poder imprimir en la terminal el valor de la direccion de memoria RAM de la variable, no necesariamente van a ser las mismos valores siempre

# The variable "Y" is assigned a value of 10, but where we know
# the value of the variable is stored, the values ​​are stored
# With this function you can see the value in memory that the variable has
#This is used to print the RAM memory address of the variable to the terminal; the values ​​will not necessarily always be the same.

#_____________________________________________________________________________________________________________________________________________________________________________

# Tipo de datos de Python
# Python type of data 

# Numeric/ Numerico
# Hay tres tipos de estos datos 
# Python have tre types of this data

Integer = 12
Float = 1.34
Complex = complex(3, 4j)

print(Integer)

print(Float)

print(Complex)

# Dictionary/ Dicionario

persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Nueva York"
}

# Boolean/ Booleano

es_mayor_de_edad = True
esta_activo = False

# Set

Lista = set([3,2,7,6,4,4,3,4])

# Secuencie type


