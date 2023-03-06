a=16
b=25
c=27
#test expression
if a<=b:
    print(b)

#La salida siempre tiene que estar tabulada, sino cogerá la siguiente línea de código
if a<=0:
    print(a)
print(b)

#Uso de else

if a >= b:
    print(a)
else:
    print(b)

#Elif - Else if, permite agregar varias condiciones
if a >= b:
    print("a is greater than or equal to b")
elif a == b:
    print("a is equal to b")

#Cominación de todas ellas
if a>b:
    print("a is greater than b")
elif a<b:
    print("b is greater than a")
else:
    print("a is equal to b")

#Lógica condicional anidada
if a>b:
    if b>c:
        print("a is greater than b and greater than c")
    else:
        print("a is greater than b and less than c")
elif a==b:
    print("a is equal to b")
else:
    print("a is less than b")

#Operador or
if a==16 or b==16:
    print(a+b)

#Operador and
if a==16 and b!=16:
    print(a+b)
    