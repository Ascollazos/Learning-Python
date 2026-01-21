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


def evaluar_dia(dia):
    match dia:
        case "lunes":
            print("Es lunes, ¡a trabajar!")
        case "viernes":
            print("¡Casi es fin de semana!")
        case _: # El caso por defecto (similar a 'else' o 'default')
            print("Es otro día de la semana.")

evaluar_dia("lunes")
evaluar_dia("domingo")
