# Tipos de operadores logicos en python
# Types of logical operators in Python

# sirven para comparar dos expreciones booleanas, una exprecion de la lado izquierdo y otra exprecion del lado derecho 

#operador/                   Descripcion                     /     Uso

# and     Devuelve true si anbos operadores son true             A and B

# or      Devuelve true si uno de los operadores son true        A or B

# not     Devuelve true si alguno de lo operadores es false      A not B 

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
Valor = int(input("Escribe el valor"))
valorminimo = 0
valormaximo = 5

dentroDeRango = (Valor >= valorminimo) and (Valor <= valormaximo)

if dentroDeRango:
    print(f'El valor {Valor} esta dentro de rango')
else:
    print(f'El valor {Valor} esta fuera de rango')

# Ejercicio de Pyhton con el operador or

vacaciones = False
diaDeDescanso = False

if not (vacaciones or diaDeDescanso) :
    print('Puede asistir al juego')
else:
    print('Tiene deberes por hacer')

edad = int(input('Introduce tu edad: '))

veintes = edad >= 20 and edad < 30
print("veintes")
treintas = edad >= 30 and edad <40
print("treintas")

if veintes or treintas:
    print('Dentro del rango (20\'s) o (30\'s)')
else:
    print("No esta dentro de los 20's ni de los 30's")