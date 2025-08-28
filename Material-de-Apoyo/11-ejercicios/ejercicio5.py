"""
Ejercicio 5.
Crear una lista con el contenido de esta tabla:

ACCION      AVENTURA        DEPORTES
GTA         ASSINS          FIFA 21
COD         CRAHS           PRO 21
PUG         PRINCEOPF       MOTO GP 21

Mostrar esta informacion ordenada
"""
tabla = [
    {
        "categoria" : "ACCION",
        "juegos" : ["GTA", "COD", "PUG"]
    },

    {
        "categoria" : "AVENTURA",
        "juegos" :["ASSINS", "CRASH", "Prince Of Persia"]
    },
    {
        "categoria" : "DEPORTE",
        "juegos" :["FIFA 21", "PRO 21", "MOTO 21"]
    }
    ]

print(tabla)

for videojuegos in tabla:
    print(f"\n___________Categoria: {videojuegos['categoria']}___________")
    print(f"Juegos: {videojuegos['juegos']}")


for categoria in tabla:
    print(f"\n___________Categoria: {categoria['categoria']}___________")
    
    for juego in categoria['juegos']:
        print(f"Juegos: {juego}")