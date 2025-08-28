"""
Ejercicio 4.
Crear un script que tenga 4 variables, una lista, un str, un int, y booleano y que imprima un mensaje segun el tipo de dato de cada variable. Usar funciones
"""

def traducirTex(tipo):

    if tipo == list:
        result = "Lista"

    elif tipo == str:
        result = "Cadena de texto"
    
    elif tipo == int:
        result = "Entero"

    elif tipo == bool:
        result = "Booleano"
    
    return result


def comprobar(dato,tipo):
    test= isinstance(dato,tipo)
    result = ""

    if test:
        result = f"Este dato el del tipo: {traducirTex(tipo)}"
    
    else:
        result = "Este dato no es de este tipo"

    return result


mi_lista = [1, "Albis", "Kenia", 23]
mi_str = "Hola, mundo"
mi_int = 23
mi_booleano = True

print(comprobar(mi_lista, list))
print(comprobar(mi_str, str))
print(comprobar(mi_int, int))
print(comprobar(mi_booleano, bool))