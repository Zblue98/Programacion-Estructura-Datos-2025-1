"""
Ejercicio 3. Programa que compruebe si uan variable esta vacia
y si esta vacia, rellenarlo con texto en minuscula y mostrarlo
en mayusculas
"""

texto = ""


if len(texto.strip())<=0:

    texto = input(str("Rellene la variable: "))
    print(texto.upper())

else:
    print(f"La variable tiene contenido: {texto}")
