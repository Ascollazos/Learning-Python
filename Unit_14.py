numero = int(input("Proporciona un numero entero entre 1 y 3: "))
if numero == 1:
    numeroTexto = "Numero uno"
elif numero == 2:
    numeroTexto = "Numero dos"
elif numero == 3:
    numeroTexto = "Numero tres"
else:
    numeroTexto = "Valor fuera de rango"

print(f'El numero proporcionado: {numero} - {numeroTexto}') 
