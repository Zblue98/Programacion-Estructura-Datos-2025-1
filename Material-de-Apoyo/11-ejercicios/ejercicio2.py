"""
Ejercicio 2. Escribir un programa que anada valores a una lista mientras su longitud sea menor a 120 y luego mostrar la lista.
Plus: Usar while y for
"""

# Solucion con Bucle For
coleccion = []

for contador in range (0, 120):
    coleccion.append(f'elemento - {contador}')
    print("Mostrando el: " + coleccion[contador])

print(coleccion[119])

# Solucion con Bucle While

coleccion = []
contador = 0
while contador < 120:
    coleccion.append(f'elemento - {contador}')
    print("Mostrando el: " + coleccion[contador])
    contador += 1
print(coleccion[117])