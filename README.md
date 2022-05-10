Conceptos de funciones que vienen dentro del programa de python:

.upper() - Convierte todo el texto a mayusculas

.capitalize() - Convierte la primer letra en mayuscula

.strip() - Borra los espacios basura

.replace() - remplaza el primer parametro que le demos dentro del parentesis con el segundo

len - Ver cuantos caracteres tiene una string

.append() - Agrego un elemento a una lista

.pop() - Borro elementos de una lista

En python a comparacion de C dentro de una lista(array), puedo tener diferentes elementos de diferentes tipos, es decir, puedo poner un caracter, una string, un numero entero, etc.

Las listas son dinamicas, ocupan mas memoria, y se usa []. En cambio, las tuplas son estaticas, eso quiere decir que no puedo usar append ni pop, al ser estaticas ocupan menos memoria y se identifican con ()

Las tuplas son inmutables(no puede cambiar), asi como las strings. Las listas son mutables(si pueden cambiar). Esa es la diferencia que tienen

Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

Operaciones en diccionarios:

.keys():Retorna la clave de nuestro elemento.

.values(): Retorna una lista de elementos (valores del diccionario).

.items(): Devuelve lista de tuplas (primero la clave y luego el valor).

.clear(): Elimina todos los items del diccionario.

.pop(“n”): Elimina el elemento ingresado.
-------------------------------------------------------------

FIFO (primero en entrar, primero en salir)
FILO (primero en entrar, último en salir)
LIFO (último en entrar, primero en salir)
LILO (último en entrar, último en salir)
