# Operaciones aritméticas en Python
---
En este módulo, exploraremos las principales funcionalidades matemáticas de Python:

- Los operadores matemáticos disponibles en Python.
- El orden de las operaciones.
- Cómo convertir cadenas en números.

Suma (+), Resta (-), Multiplicación(*), División (/)
- División de múltiplo inferior (//) = **redondear hacia abajo**
- Cálculo del resto de una división (%)

```
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17
# 22
```

## Uso de números en Python
---
### Conversión de cadenas en números
Python admite dos tipos principales de números: números enteros (o `int`) y número de punto flotante (o `float`).
Diferencia:  La existencia de un separador decimal en los float
Si usa un valor no válido para int o float, recibirá un error.


### Valores absolutos
Use `abs` para convertir el valor negativo en su valor absoluto
```
print(abs(39 - 16))
print(abs(16 - 39))

# Output
# 23
# 23
```

### Redondeo
Función integrada de Python denominada `round`. Para redondear hacia arriba
```
print(round(14.5))

# Output: 15
```

### Biblioteca matemática
Para proporcionar operaciones y cálculos más avanzados
`math` permite hacer el redondeo con floor y ceil

```
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13
# 12
```
