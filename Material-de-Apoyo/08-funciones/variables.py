"""
Variables locales: Se definen dentro de la funcion y no se pueden usar fuera de lla, solo estan disponibles dentro. A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una funcion y estan disponibles dentreo y fuera de ellas.

"""

frase = 'Ni los genios son tan genios, ni los mediocres tan mediocres'

print(frase)

def holaMundo():
    frase = 'Hola, Mundo!!'
    print('Dentro de la funcion')
    print(frase)

    year = 2021
    print(year)

    global website
    website = 'albisfoxweb.es'
    print('DENTRO: ', website)

    return 'Dato devuelto ' +str(year)


print(holaMundo())
print("FUERA: ", website)