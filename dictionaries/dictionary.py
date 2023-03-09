planet = {
    "name" : "Mars",
    "moons" : 2
}

print(planet["name"],"has ",planet.get("moons")," moon(s).")

planet["circunference(km)"] = {
    "polar": 6752,
    "equatorial": 6792
}

print(f'The polar circumference of {planet["name"]} is {planet["circunference(km)"]["polar"]}')
