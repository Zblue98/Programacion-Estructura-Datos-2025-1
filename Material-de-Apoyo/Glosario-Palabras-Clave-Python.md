# 🐍 Glosario de Palabras Clave de Python 🐍

Este glosario contiene definiciones de términos clave, conceptos y palabras reservadas comunes en el lenguaje de programación Python, organizados por categorías para facilitar su consulta.

---

## 🔷 1. Control de Flujo

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `if`          | si         | Ejecuta un bloque si la condición es verdadera. |
| `elif`        | sino si    | Evalúa otra condición si `if` fue falsa. |
| `else`        | sino       | Se ejecuta si ninguna condición anterior fue verdadera. |
| `for`         | para       | Bucle que recorre una secuencia (listas, tuplas, cadenas, etc.). |
| `while`       | mientras   | Bucle que continúa ejecutándose mientras una condición sea verdadera. |
| `break`       | romper     | Sale del bucle actual inmediatamente. |
| `continue`    | continuar  | Salta a la siguiente iteración (ciclo) del bucle, omitiendo el resto del código en la iteración actual. |
| `pass`        | pasar      | No hace nada; es un marcador de posición para código futuro o funciones/clases vacías. |
| `match`       | coincidir  | Evalúa un valor contra una secuencia de patrones (disponible desde Python 3.10). |
| `case`        | caso       | Define un patrón y el bloque de código a ejecutar dentro de una sentencia `match`. |

---

## 🔷 2. Definición y Estructura

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `def`         | definir    | Declara una función. |
| `class`       | clase      | Declara una clase, una plantilla para crear objetos. |
| `return`      | devolver   | Retorna un valor desde una función y finaliza su ejecución. |
| `yield`       | producir   | Devuelve un generador (un tipo de iterador) y pausa la ejecución de la función. |
| `lambda`      | lambda     | Define una función anónima (sin nombre) o en línea. |

---

## 🔷 3. Manejo de Excepciones

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `try`         | intentar   | Inicia un bloque de código que puede generar errores (excepciones). |
| `except`      | excepto    | Maneja una excepción específica que fue lanzada dentro del bloque `try`. |
| `raise`       | lanzar     | Lanza una excepción manualmente para indicar un error o condición anormal. |
| `finally`     | finalmente | Se ejecuta siempre al final del bloque `try`/`except`, haya o no una excepción. |
| `assert`      | afirmar    | Lanza un `AssertionError` si una condición dada no es verdadera. |

---

## 🔷 4. Importación de Módulos

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `import`      | importar   | Importa un módulo o paquete completo. |
| `from`        | desde      | Importa elementos (funciones, clases, variables) específicos de un módulo. |
| `as`          | como       | Renombra un módulo o elemento importado para usar un alias más corto o diferente. |

---

## 🔷 5. Valores Lógicos y Constantes

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `True`        | verdadero  | Valor booleano verdadero. |
| `False`       | falso      | Valor booleano falso. |
| `None`        | ninguno    | Representa la ausencia de valor o un valor nulo. |

---

## 🔷 6. Operadores Lógicos y Comparación

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `and`         | y          | Verdadero si **ambas** condiciones son verdaderas. |
| `or`          | o          | Verdadero si **al menos una** condición es verdadera. |
| `not`         | no         | Niega una condición (invierte su valor booleano). |
| `in`          | en         | Verifica si un valor está contenido dentro de una secuencia (lista, tupla, cadena) o si una clave está en un diccionario. |
| `is`          | es         | Verifica si dos objetos son el mismo objeto en memoria (idénticos). |

---

## 🔷 7. Gestión de Contexto y Asincronía

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `with`        | con        | Se utiliza para manejar recursos (como archivos o conexiones) de forma segura y automática (context managers). |
| `async`       | asíncrono  | Declara una función o rutina como una corrutina (función asincrónica). |
| `await`       | esperar    | Pausa la ejecución de una corrutina hasta que otra corrutina o una operación asincrónica se complete. |

---

## 🔷 8. Otros

| Palabra Clave | Traducción | Significado |
| :------------ | :--------- | :---------- |
| `global`      | global     | Declara que una variable dentro de una función se refiere a una variable global. |
| `nonlocal`    | no local   | Declara que una variable dentro de una función anidada se refiere a una variable de un ámbito superior no global. |
| `del`         | eliminar   | Elimina una variable, un elemento de una lista o un atributo de un objeto. |
