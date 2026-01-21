# Ejercicio: tienda de libros 

"""
En es te caso el usaurio tiene que proporcionar el nombre del libro, el
ID como int, el precio del libro en float, y revisar si el envio es 
gratuito o no, por ultimo debe imprrmir la informacion

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