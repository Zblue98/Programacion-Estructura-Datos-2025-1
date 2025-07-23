"""
# BUCHLE WHILE
Esctrucutra de control que itera o repite la ejecucion de una serie de instruciones
tantas veces como sea necesar, hasta dejar de cumplir la condicion.

while condicion:
    bloque de instrucciones
    actualizacion de contador
"""

contador = 1

while contador <= 100:
    print('Estoy en el numero: ' + str(contador))
    contador += 1

print('____________________________________________________')
muestrame = str(0)
contador = 1
while contador <= 100:
    muestrame = muestrame + ', ' + str(contador)
    contador += 1

print('Los numeros naturales del ' + muestrame)


# Ejemplo

print('########### EJEMPLO ###########')

numero_usuario = int(input('De que numero quieres la tabla?: '))

contador = 0

while contador <= 10:
    print(f'{numero_usuario} X {contador} = {numero_usuario*contador} ')
    contador += 1
else:
    print('Tabla terminada')