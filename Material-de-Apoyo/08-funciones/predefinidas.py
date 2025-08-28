nombre = "Albis Fox"

#fundiones generales
print (nombre)
print(type(nombre))

#Detectar el tipado
comprobar = isinstance(nombre, str)

if comprobar:
    print("Esa variable es un String")

else:
    print("Esa variable no es una cadena")

if not isinstance(nombre, float):
    print("la variable no es un numero con decimales")

#Limpiar espacios
    
    frase = "   mi contenido"
    print(frase.strip())

#eliminar variable
year = 2024
print(year)
del (year)
#print(year)

#Comprobar variable vacia

texto = " ff "

if len(texto) <=0:
    print("La variable esta vacia")
else:
    print("La variable tiene contenido", len(texto))

#Encontrar caracteres
frase = "La vida es bella"
print(frase.find("vida"))

#Reemplazar caracteres en un string

nueva_frase = frase.replace("vida", "moto")

print(nueva_frase)

#Mayusculas y minuscuilas
print(nombre)
print(nombre.lower())
print(nombre.upper())

