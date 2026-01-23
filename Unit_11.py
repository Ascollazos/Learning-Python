# Tipos de operadores logicos en python
# Types of logical operators in Python

# sirven para comparar dos expresiones booleanas, una expresión del lado izquierdo y otra expresión del lado derecho 

#operador/                   Descripción                     /     Uso

# and     Devuelve true si ambos operadores son true             A and B

# or      Devuelve true si uno de los operadores es true         A or B

# not     Devuelve true si alguno de los operadores es false.    A not B 


# These are used to compare two Boolean expressions, one on the left and one on the right.

# operator/                  Description                     /     Use

# and     Returns true if both operators are true.               A and B

# or      Returns true if either operator is true.               A or B

# not     Returns true if either operator is false.              A not B


A = True

B = True

resultado = A and B
print(resultado)

A = False

B = False

resultado = A or B
print(resultado)

A = True

B = False

resultado = not B
print(resultado)

# Ejercicio de Python con el operador and
# Python exercise with the and operator

Valor = int(input("Escribe el valor"))
valorminimo = 0
valormaximo = 5

dentroDeRango = (Valor >= valorminimo) and (Valor <= valormaximo)

if dentroDeRango:
    print(f'El valor {Valor} esta dentro de rango')
else:
    print(f'El valor {Valor} esta fuera de rango')

# Ejercicio de Pyhton con el operador or
# Python exercise with the or operator

vacaciones = False
diaDeDescanso = False

if vacaciones or diaDeDescanso :
    print('Tiene deberes por hacer')
else:
    print('Puede asistir al juego')

if not (vacaciones or diaDeDescanso) : # Utilizamos el operador not para invertir los valore de las variables ya sean true o false
    print('Tiene deberes por hacer')   # # We use the not operator to invert the values ​​of variables, whether true or false
else:
    print('Puede asistir al juego')

# Ejercicio con los operadores and y or
# Exercise with the AND and OR operators

edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print("veintes")
treintas = edad >= 30 and edad <40
print("treintas")

if veintes or treintas:
    print('Dentro del rango (20\'s) o (30\'s)')
    if veintes :
        print ('Dentro del reango de los 20\'s')
    elif treintas :
        print('Dentro de los 30\'s')
    else:
        print('Fuera de rango')
else:
    print("No esta dentro de los 20's ni de los 30's") 



# Mejoras respecto a la sintaxis del  manejo de operadores lógicos
# Improvements to the syntax for handling logical operators

if (edad >= 20 and edad < 30 ) or (edad >= 30 and edad < 40):
    print("Dentro de los rangos de los (20's) o (30's)") 

# Corrección
# Correction

if ( 20 <= edad < 30 ) or ( 30 <= edad < 40):
    print("Ahora esta mejor ")
