# Ejercico que tal estubo tu Dia Puntua del 1 al 10
# Exercise How was your day Rate it from 1 to 10

Puntaje = int(input("Del 1 al 10 que tal estubo tu dia? "))

if Puntaje == 6:
    print("Parece que tu dia trascurrio sin muchos contratiempos")
elif Puntaje >= 7:
    print("Me alegro que hayas tenido un buen dia")
elif Puntaje == 5:
    print("Espero que mañana sea un mejor dia")
elif Puntaje <= 4 and Puntaje > 0:
    print("Siento que hayas tenido un mal dia, espero que mañana sea mejor")
else:
    print("Valor no valido, por favor ingresa un numero del 1 al 10")