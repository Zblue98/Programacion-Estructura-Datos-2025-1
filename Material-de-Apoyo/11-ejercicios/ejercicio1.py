"""
Ejercicio1. Hacer un programa que tenga una lista
de 8 numeros enteros y haga lo siguiente:
- (hecho) Recorrer la lista y mostrarla
- (hecho) Hacer una funcion que recorra listas de numero u devuelva un string
- (hecho) Ordenarla y mostrarla
- (hecho) Mostrar su longitud
- (hecho)Buscar algun elemento(Que el usuario pida por teclado)
"""

# Crear la lista

numeros =[13, 64, 52, 73, 21, 7, 91, 63]

# Recorrer y mostrar lista
print("############# Recorrer y mostrar #############\n")
for numero in numeros:
    print(numero)

# Funcion de recorrer y duevuelve string
print("############# Recorrer y mostrar #############\n")
def mostrarLista(lista):
    #lista.sort()
    resultado = ""

    for elemento in lista:
        resultado += "Elemento: " + str(elemento) + "\n"
    
    return resultado

print(mostrarLista(numeros))

# Ordenar y mostrar
print("############# ordenar y mostrar #############\n")
numeros.sort()
print(mostrarLista(numeros))

# Mostrar su longitud
print("############# Mostrar su longitud #############\n")
print(len(numeros))

try:
    # Buscar en la lista
    print("############# Buscar en la lista #############\n")

    busqueda = int(input("Introduce el numero: "))

    comprobar = isinstance(busqueda, int)

    while not comprobar or busqueda <= 0:
        busqueda = int(input("Introduce el numero: "))

    else:
        print(f"Has introducido el numero {busqueda}")

    print(f"##### Buscando en la lista el numero {busqueda} #####")

    search = numeros.index(busqueda)

    print(f"El numero {busqueda} existe en la lista, es el indice: {search}")
except:
    print("El numero no esta en la lista")