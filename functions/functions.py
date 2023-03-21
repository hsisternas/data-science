def rocket_parts():
    print("payload, propellant, structure")

output = rocket_parts()
# payload, propellant, structure
output is None
# True

#En Python, si una función no devuelve explícitamente un valor, devuelve implícitamenteNone. Actualizar la función para devolver la cadena en lugar de imprimirla hace que la variable output tenga un valor distinto:

def rocket_parts():
    return "payload, propellant, structure"

output = rocket_parts()
#output
#'payload, propellant, structure'


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
    

def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

total_days = days_to_complete(238855, 75)
round(total_days)
#133

round(days_to_complete(238855, 75))
#133

# ---

from datetime import timedelta, datetime

def arrival_time(hours=0):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")

print(arrival_time())

def arrival_time_2(destination, hours=51):
    now = datetime.now()
    arrival_2 = now + timedelta(hours=hours)
    return arrival_2.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time_2("Moon"))
print(arrival_time_2("Orbit", hours=0.13))

#-----

#La función siguiente imprime los argumentos recibidos:

def variable_length(*args):
    print(args)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"  

print(sequence_time(4,14,18))  
#'Total time to launch is 36 minutes'   
print(sequence_time(4,14,48))
#'Total time to launch is 1.1 hours'


def variable_length(**kwargs):
    print(kwargs)
    
print(variable_length(tanks=1, day="Wednesday", pilots=3))

def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
print(crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins"))