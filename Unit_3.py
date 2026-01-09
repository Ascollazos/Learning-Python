mi_cantante_favorito_es = "milo_j"
comentario_1 = "THE BESTS SINGER ON THIS TIME"
comentario_2 = "EL MEJOR CANTANTE DE ESTE TIEMPO"


print("My favorite singer is:", mi_cantante_favorito_es , comentario_1 )
print("Cantante favorito es: "+ mi_cantante_favorito_es+ " " + comentario_2 )

# De esta manera se pueden concatenar variables de tipo str en un print en python
# Cuando lo intentas hacer con variable de tipo numerico te suma los numeros sino que los concatena
# amenos de que los encierres en comillas pasrian a ser variables de tipo str

# This is how you can concatenate string variables in a print statement in Python
# When you try to do this with numeric variables, it adds the numbers instead of concatenating them
# Unless you enclose them in quotes, they would become string variables

# Example
# Ejemplo

numero_1 = 1
numero_2 = 2

print( numero_1 + numero_2 )

numero_1 = "1"
numero_2 = "2"

print("Uno concatenado con dos es igual a " + numero_1 + numero_2 )


# Ahora veremos los valores booleanos
# Los tipos booleanos nos va a permitir saber si un valor es verdadero o falso
# En Python estas variables son representadas por los valores de True y False que se traducen en verdadero y falso
# lo que hacen estas expresiones es permitirnos tomar una decisión por ejemplo

# Now we'll look at Boolean values
# Boolean types allow us to know if a value is true or false
# In Python, these variables are represented by the values ​​True and False
# These expressions allow us to make a decision For Example


mi_variable = False
second_variable = True

mi_variable = 3 > 2
print(mi_variable)

if mi_variable:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")
    
# Como procesar la entrada de datos en Python
# La función input sirve para solicitar a un usuario que proporcione un valor
# Podemos usar la función input como una variable para imprimirla en la terminal o usarla con otras funciones

# How to process data input in Python
# The input function is used to request a value from a user
# We can use the input function as a variable to print it to the terminal or use it with other functions

User_name = input("Porfa ingrese su nombre: ")
print("Hola", User_name) 
print("Fin del programa")

# Tambien se pueden hacer operaciones con los datos pedios al usuario 
# Agregando cieras funciones delante de la funcion input

num_1 = int(input("Escribe el primer numero"))
num_2 = int(input("Escribe el segundo numero"))
num_3 = int(input("Write the fourth number"))
num_4 = int(input("Write the fifth number"))

result = num_1 + num_2 - num_3 * num_4

print(result)
