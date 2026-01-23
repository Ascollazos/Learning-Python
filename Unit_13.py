# Ejercicio: tienda de libros 

"""
En este caso el usuario tiene que proporcionar el nombre del libro, 
él Id como int, el precio del libro en float, y revisar si el envío
es gratuito o no, por último debe imprimir la información

"""

# Exercise: Bookstore

"""
In this case, the user has to provide the book's name, the ID as an 
integer, the book's price as a float, and check if shipping is free 
or not. Finally, they must print the information.

"""

print("Proporcione los siguentes datos del libro: ")
nombre = input("Proporciones el nombre del libro: ")
Id = int(input("Proprciona el ID del libro: "))
precio = float(input("Proporciona el valor del libro: "))
enviogratis = input("Indica si el envio es gratuito (True/False)")

if enviogratis == "True":
    enviogratis == True
    Aplica = "Si"
elif enviogratis == "False":
    enviogratis== False
    Aplica = "No"
else:
    print("Valor incorrecto, debe escribir True O False")

print(f'''
Nombre: {nombre}
ID: {Id}
Precio:{precio}
Envio_gratuito?: {Aplica}
''')