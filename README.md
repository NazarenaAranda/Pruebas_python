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

Con random la computadora busca un valor random de lo que nosotros le aclaremos, en el caso del diccionario usamos random.choice porque lo que queremos es un caracter de cualquier tipo. Con random.randint() nos busca un numero random.

Filter: filtra los datos de una lista retornando solo los que son True

Map: manipula los datos de una lista

Reduce: opera los datos de una lista entre sí para obtener 1 solo resultado

ENTORNO VIRTUAL
---------------

Un entorno virtual es un programa asilado que tiene sus propios modulos. Esto se hace para que si hay una actualizacion y sacan algo que nosotros usamos no se nos rompa.

Git init - inicializa un repositorio vacio de github

Al querer ingresar a python3 desde nuestra funcion si ponemos la flag -m (es un indicativo que dice que vamos a modificar el funcionamiento original. -m es el modulo interno del lenguaje) y "venv" es el modulo que significa entorno virtual. Luego de esto va el nombre que le queremos poner al entorno, generalmente se pone (venv).

Luego de hacer esto, nos va a aparecer varias carpetas adentro de nuestro entorno, nosotros vamos a tocar Script porque ahi es donde esta el comando para activar nuestro entorno virtual

-------------------------------------------------------------

FIFO (primero en entrar, primero en salir)
FILO (primero en entrar, último en salir)
LIFO (último en entrar, primero en salir)
LILO (último en entrar, último en salir)
