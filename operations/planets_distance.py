first_planet = 149597870
second_planet = 778547200

distance_km = second_planet - first_planet
print(distance_km)

distance_mi = distance_km / 1.609344
print(distance_mi)

####### Planets distance

first_planet_input = input("Enter the distance from the sun for the first planet in KM: ")
second_planet_input = input("Enter the distance from the sun for the second planet in KM: ")

planet_1 = int(first_planet_input)
planet_2 = int(second_planet_input)

distance = planet_2 - planet_1
print(abs(distance))


