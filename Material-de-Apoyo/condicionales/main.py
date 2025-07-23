"""
Condicional IF

SI se_cumple_esta_condicion:
    Ejecutar grupo de instruciones
SI NO:
    Se ejecutan otro grupo de instruciones

if condicion:
    instruciones
else:
    otras instruciones

# Operadores de comparacion
== Igual igual
!= diferente
< menor que
> mayor que
<= menor o igual que
>= mayor o igual que

# Operadores logicos

and Y
or O
! Negacion
not NO
"""


# Ejemplo 1
print('***************** EJEMPLO 1 ******************')

color = 'rojo' #input('Adivina cual es mi color favorito: ')

if color == 'rojo':
    print('Enhorabuena!!'+ '\n' +'El color es ROJO')
else:
    print('El color es incorrecto')


# Ejemplo 2
print('\n***************** EJEMPLO 2 ******************')


year = 2020
#year = int(input('En que año estamos?: '))

if year >= 2021:
    print('Estamos de 2021 en adelante')

else:
    print(f'{year} es un año anterior a 2021')

# Ejemplo 3
print('\n***************** EJEMPLO 3 ******************')

nombre = 'Albis Fox'
ciudad = 'Quibdo'
contienete = 'America'
edad = 23
mayoria_edad = 18

if edad >= mayoria_edad:
    print(f'{nombre} es mayor de edad!!')

    if contienete != 'America':
        print('El usuario no es Americano')
    else:
        print(f'El usuario es Americano y de {ciudad}')

else:
    print(f'{nombre} No es mayor de edad!!')

# Ejemplo 4
print('\n***************** EJEMPLO 4 ******************')

dia = 3 #int(input('Di el dia de la semana: '))

if dia == 1:
    print('Es Lunes')
elif dia == 2:
    print('Es Martes')
elif dia == 3:
    print('Es Miercoles')
elif dia == 4:
    print('Es Jueves')
elif dia == 5:
    print('Es Viernes')
elif dia == 6:
    print('Es Sabado')
elif dia == 7:
    print('Es Domingo')
else:
    print('No corresponde a ningun dia de la semana')

# Ejemplo 5
print('\n***************** EJEMPLO 5 ******************')

edad_minima = 18
edad_maxima = 65
edad_oficial = 23 #int(input('Cual es tu edad?: '))

if edad_oficial >= 18 and edad_oficial <= 65:
    print('Estas en edad para poder trabajar!!')
else:
    print('No estas en edad de poder trabajar')

# Ejemplo 6
print('\n***************** EJEMPLO 6 ******************')

pais = 'Colombia'

if pais == 'Mexico' or pais == 'España' or pais == 'Colombia':
    print(f'{pais} es un pais de habla hispana')

else:
    print(f'{pais} No es un Pais de habla hispana')

# Ejemplo 7
print('\n***************** EJEMPLO 7 ******************')

pais = 'Colombia'

if not (pais == 'Mexico' or pais == 'España' or pais == 'Colombia'):
    print(f'{pais} No es un pais de habla hispana')

else:
    print(f'{pais} Si es un Pais de habla hispana')

# Ejemplo 8
print('\n***************** EJEMPLO 8 ******************')


pais = 'Colombia'

if pais != 'Mexico' and pais != 'España' and pais != 'Colombia':
    print(f'{pais} No es un pais de habla hispana')

else:
    print(f'{pais} Si es un Pais de habla hispana')

