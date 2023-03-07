# Introducción a las listas en Python
En este módulo, descubrirá cómo usar listas y cuáles son las tareas más comunes con ellas.

**Objetivos**
- Identificar cuándo se debe usar una lista.
- Crear una lista con valores de cadena y valores numéricos.
- Acceder a un elemento determinado de una lista mediante índices.
- Insertar elementos al final de una lista.
- Ordenar y segmentar una lista.

## Intro
Almacenar cada valor en una variable individual hace que el código sea más difícil de leer y escribir. Para almacenar varios valores, puede usar una lista de Python.

## Presentación listas
### Crear una lista
Cada valor está separado por una coma y están entre corchetes `[]`
```
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
```
### Acceso a elementos
Se puede acceder o modificar cualquier valor de la lista introduciendo el **índice** en los corchetes:
```
print(planets[0])
# Output: Mercury

planets[3] = "Red Planet"
print(planets[3])
# Output: Red Planet 
```
***Dado que todos los índices empiezan por 0, [1] es el segundo elemento, [2] es el tercero, etc.***

### Longitud
Para obtener la longitud usar la función `len()`

```
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

# Output:
# There are 8 planets in the solar system
```

### Incorporar y eliminar valores
Para añadir valores al final de la lista `.append(value)`

```
planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

# Output:
# There are actually 9 planets in the solar system.
```

Para eliminar el último valors usar `.pop()`

```
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
```

---
Índices positivos van de principio a final [0,1,2,3...]
Índices negativas van del final al inicio [-1,-2,-3...]

```
print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

# Output
# The last planet is Neptune
# The penultimate planet is Uranus
```
---

### Búsqueda de un valor en la lista
Usar el método `index` -> Busca el valor y devuelve el índice

```
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

# Output
# Jupiter is the 5 planet from the sun
```

## Almacenamiento de números en listas
Mismo funcionamiento que en querys, pero debe utilizarse tipo `float`
Ejemplo:
` gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]`

### Uso de `min` y `max` con listas
La función max() devuelve el número más grande y min() devuelve el más pequeño. Por lo tanto, `min(gravity_on_planets)` devuelve el número más pequeño de la lista `gravity_on_planets`, que es 0,377 (Marte).


## Manipulación de datos de lista

### Segmentación
Para obtener los planetas **antes** de la tierra:
```
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

# Output: ['Mercury', 'Venus']
```
La Tierra no está incluida en la lista. El motivo es que el índice finaliza antes del índice final.

Para obtener los planetas **después** de la tierra
```
planets_after_earth = planets[3:8]
print(planets_after_earth) 

# Output
# ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
```

Si no coloca el índice de detención en la segmentación `[3:]`, Python asume que quiere ir al final de la lista


**Una segmentación crea una lista nueva. No modifica la lista actual.**

### Combinación de listas
Con el operador `+` en dos listas para devolver una nueva

```
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']
```

### Ordenación de listas
Use el método `.sort()` para ordenar en orden numérico o alfabético según el tipo de lista
````
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']
````
Y para hacerlo en orden inversio usar `.sort(reverse=True)`
````
regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

# Output
# The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']
````
**El uso de sort modifica la lista actual.**