#Variables
sum=1+2
print(sum)

print("show this in console")

product = sum*2
print(product)

#Tipos de datos
planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

#Operadores
#<left side> <operator> <right side>
left_side = 10
right_side = 5
left_side / right_side # 2

#Operadores de asignación
planets_in_solar_system *= 2
print(planets_in_solar_system)

planets_in_solar_system /= 2
print(planets_in_solar_system)

#Fechas
from datetime import date
date.today()

#Conversión de tipos de datos
print("Today's date is: " + str(date.today()))


#Ejercico conversor de unidades 1
parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

#Llamadas a diferentes argumentos
import sys
print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
