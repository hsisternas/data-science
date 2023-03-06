name = "Ganymede"
planet = "Mars"
gravity = "1.43"
template = """Gravity facts about {name}
--------------------------
Planet name: {name}
Grabity on {name}: {gravity} m/s2"""

print(template.format(name=name, planet=planet, gravity=gravity))
