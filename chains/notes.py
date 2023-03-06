fact = "La luna no tiene atmosfera"
fact + "Nada puede ser escuchado en la luna"

print(fact)

# Al agregar cadenas, Python no modifica ninguna, sino que devuelve una cadena nueva como resultado
two_facts= fact + ". Nada puede ser escuchado en la luna"
print(two_facts)

#Cuando el texto tiene una combinación de comillas simples y dobles, puede usar comillas triples para evitar problemas con el intérprete:
"""We only see about 60% of the Moon's surface, this is known as the "near side"."""

# TEXTO MULTILÍNEA
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

multiline2 = """Facts about the Moon:
There is no atmosphere
There is no sound."""

print(multiline2)

#DIVISIÓN DE CADENA
#Si no le ponemos argumento, cortará en cada espacio

temperatures = """Daylight: 260 F
Nighttime: -280 F"""
temperatures .split()
###Salida: 'Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']
temperatures .split('\n')
#Cortará en cada salto de línea
###Salida: ['Daylight: 260 F', 'Nighttime: -280 F']


#BÚSQUEDA DE UNA CADENA
#Parámetros: in / .find() / .count()

"Moon" in "lo que sea" 
"Moon" in "La Moon mola mucho" 


temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""

temperatures.find("Moon")
#Salida: -1 (No ha encontrado la cadena de carácteres)

temperatures.find("Mars")
#Salida: 65

temperatures.count("Mars")
#Salida: 1

#Recomendación: uso de .lower() en la cadena de texto para que al usar .count no haya distinciones entre mayúsculas y minúsculas


#COMPROBACIÓN DE CONTENIDO
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
#parts
#Salida:['Mars average temperature', ' -60 C']
parts[-1]
#Salida:' -60 C'

mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
#Salida: 30

#.isnumeric() o .isdecimal() OJO no funcionarán con valores negativos

"-60".startswith('-')
if "30 C".endswith("C"):
    print("This temperature is in Celsius")


#TRANSFORMAR TEXTO
"Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
#Salida: 'Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C.'

text = "Temperatures on the Moon can vary wildly."
"temperatures" in text
#False
"temperatures" in text.lower()
#True

moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
'\n'.join(moon_facts)
'The Moon is drifting away from the Earth.\nOn average, the Moon is moving about 4cm every year'

#.join() para unir pedazos


#Signo porcentaje para llamar a variables
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
#Salida: On the Moon, you would weigh about 1/6 of your weight on Earth

#Método .format() El más adecuado 👇
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
#Salida: On the Moon, you would weigh about 1/6 of your weight on Earth
print("""You are lighter on the {0}, because on the {0} 
... you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
#Salida: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth
print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
#Salida: You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth


#Método fstring
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
#Salida: On the Moon, you would weigh about 1/6 of your weight on Earth
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
#Salida: On the Moon, you would weigh about 16.7% of your weight on Earth
subject = "interesting facts about the moon"
f"{subject.title()}"
#Salida: 'Interesting Facts About The Moon'