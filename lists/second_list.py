planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Neptune"]

user_planet = input("Elija nombre del planeta (Usa mayúscula al inicio): ")

planet_index = planets.index(user_planet)

print("Estos son los planetas más cercanos que: " + user_planet)
print(planets[0:planet_index])

print("Estos son los planetas más lejanos que: " + user_planet)
print(planets[planet_index+1:])



