"""
#FOR

for variable in elemento_iterable (lista, rango, etc)
    BLOQUE DE INSTRUCCIONES

"""
contador = 0
resultado = 0

for contador in range(0,10):
    print('Voy por el '+ str(contador))

    resultado += contador

print(f'El resultado es {resultado}')

# Ejemplo tablas de multiplicar
print('\n################## EJEMPLO ###################')

numero_usuario = int(input('De que numero quieres ver la tabla?'))
num1 = int(input('\nDesde que numero quieres iniciar la multiplicacion?: '))
num2 = int(input('\nEn que numero quieres terminar la multiplicacion?: '))

for numero_tabla in range(num1,num2+1):
    """
    if numero_usuario == 453:
        print('\nNo se puede mostrar numero prohibidos')
        break
    """

    print(f'{numero_usuario} X {numero_tabla} = {numero_usuario*numero_tabla}  ')


else:
    print('Tabla terminada')