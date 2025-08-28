"""
Una variable es un contenedor de informacion
que dentro guarda un dato, de pueden crear
muchas variables y que cada una tenga un dato distinto.
"""
#Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "Con Albis Fox"
numero = 45
decimal = 6.7

# Mostrar variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print('_______________________________________')

# Sustituir el valor de algunas variables / reasignando valores 
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print('_______________________________________')

# Concadenacion
nombre = 'Albis'
apellidos = 'Fox'
web = 'albisfoxweb.com'

print(nombre + " " + apellidos + " - " + web )
print(f'{nombre} {apellidos} - {web}')
print('Hola me llamo {} {} y mi web es: {}'.format(nombre,apellidos,web))
print(nombre, apellidos, web)