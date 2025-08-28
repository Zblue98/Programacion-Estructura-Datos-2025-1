"""
FUNCIONES:
Una funcion es un conjunto de instrucciones agrupadas bajo un nombre concreto que puede reutilizarse invocando a la funcion tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
    #BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)
"""

#Ejemplo 1

print('#############   EJEMPLO 1   #############')

#Definir funcion
def muestraNombre():
    print('Victor')
    print('Paco')
    print('Juan')
    print('Francisco')
    print('Aitor')
    print('Nestor')
    print('\n')

#Invocar funcion

muestraNombre()
print('\n')

#Ejemplo 2
print('#############   EJEMPLO 2   #############')


def mostrarTuNombre(nombre, edad):
    print(f'Tu nombre es: {nombre}')
    if edad >= 18:
        print('Y este usuario es mayor de edad')


nombre = input("Introduce tu nombre: ")
edad = int(input("Introduces tu edad: "))
mostrarTuNombre(nombre,edad)

print('\n')


#Ejemplo 3
print('#############   EJEMPLO 3   #############')


def tabla(numero):
    print(f'Tabla del numero: {numero}')

    for contador in range (11):
        operacion = numero * contador
        print(f'{numero} x {contador} = {operacion}')
    print('\n')

tabla(4)
tabla(7)

#Ejemplo 3.1
for num_tabla in range (1,11):
    tabla(num_tabla)

print('\n')

#Ejemplo 4
print('#############   EJEMPLO 4   #############')

#parametro opcionales

def getEmpleado(nombre, dni=False):
    print('EMPLEADO')
    print(f'Nombre: {nombre}')
    
    if dni != 0:
        print(f'DNI: {dni}')

getEmpleado('Albis Fox')
print('\n')

#Ejemplo 5
print('#############   EJEMPLO 5   #############')

#return o devolver datos

def saludame(nombre):
    saludo = f'Hola, saludos {nombre}'

    return saludo

print(saludame('Albis Fox'))
print('\n')

#Ejemplo 6
print('#############   EJEMPLO 6   #############')

def calculadora(numero1, numero2, basicas = False):
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2

    cadena = ""
    
    if basicas != False:
        cadena += "Suma: " + str(suma) + "\n"
        cadena += "Resta: " + str(resta) + "\n"
    else:
        cadena += "Multiplicacion: " + str(multiplicacion) + "\n"
        cadena += "Division: " + str(division) + "\n"

    return cadena

print(calculadora(5,5))
print('\n')

#Ejemplo 7
print('#############   EJEMPLO 7   #############')

def getNombre(nombre):
    texto = f'Él nombre es: {nombre}'
    return texto
def getApellido(apellido):
    texto = f'Los apellidos son: {apellido}'
    return texto

def devuelveTodo(nombre, apellido):
    texto = f'{getNombre(nombre)} \n{getApellido(apellido)}'
    
    return texto
print(devuelveTodo('Albis', 'Fox'))
print('\n')

#Ejemplo 8
print('#############   EJEMPLO 8   #############')
#funciones lambda
dime_el_year = lambda year: f'El año es {year}'

print(dime_el_year(2034))