"""
# EJERCICIO 1
Pedir dos numeros al usuario y hacer todos las operaciones basicas
de una calculadora y mostrarlos por pantalla.
"""

num1 = float(input('Digite su primer numero: '))
num2 = float(input('Digite su segundo numero: '))

print(f'\n La suma es = {num1 + num2} \n La resta es = {num1 - num2} \n La multiplicacion es = {num1 * num2} \n La divicion es = {num1 / num2} ')


"""
# EJERCICIO 2
Hacer un programa que muestre todos los numeros entre dos numeros
que digite el usuario
"""
num1 = int(input('Inserte numero: '))
num2 = int(input('Inserte numero: '))

if num1 < num2:
    for numero in range(num1,num2+1):
        print(numero)
        numero += 1
else:
    for numero in range(num2,num1+1):
        print(numero)
        numero += 1


"""
 # EJERCICIO 3
Mostrar todas las tablas de multiplicar del 1 al 10, mostrando el titulo de la tabla
y luego la multiplicacion del 1 al 10.
"""

for contador in range(1,11):
    print(f'\nEsta es la tabla del {contador}')
    for multiplicacion in range(1,11):
        print(f'{contador} X {multiplicacion} - {multiplicacion * contador}')
    

"""
# EJERCICIO 4
Hacer una calculadora de porcentaje
"""
porcentaje = float(input('Que porcentaje desea saber?: '))
numero = float(input('\nA que numero quiere sacarle el porcentaje?: '))

print(f'\nEl {porcentaje}% de {numero} es {porcentaje/100*numero}')

"""
#EJERCICIO 5: Hacer un programa que pida numeros al usuario indefinidamente hasta ingresar el numero 111
"""

contador = 1
while contador < 100:
    numero = int(input('Introduce un numero: '))

    if numero >= 111:
        break
    else:
        print(f'Has introducido el numero {numero}')
