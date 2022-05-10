Conceptos de funciones que vienen dentro del programa de python:
--------------------------------------------------------------

.upper() - Convierte todo el texto a mayusculas

.capitalize() - Convierte la primer letra en mayuscula

.strip() - Borra los espacios basura

.replace() - remplaza el primer parametro que le demos dentro del parentesis con el segundo

len - Ver cuantos caracteres tiene una string

.append() - Agrego un elemento a una lista

.pop() - Borro elementos de una lista

round(nombre de que queremos redondear, x) -  redonde el numero x de los lugares que le aclaramos

Listas y Tuplas:
--------------

En python a comparacion de C dentro de una lista(array), puedo tener diferentes elementos de diferentes tipos, es decir, puedo poner un caracter, una string, un numero entero, etc.

Las listas son dinamicas, ocupan mas memoria, y se usa []. En cambio, las tuplas son estaticas, eso quiere decir que no puedo usar append ni pop, al ser estaticas ocupan menos memoria y se identifican con ()

Las tuplas son inmutables(no puede cambiar), asi como las strings. Las listas son mutables(si pueden cambiar). Esa es la diferencia que tienen

Los diccionarios en Python son una estructura de datos mutable las cuales almacenan diferentes tipos de valores sin darle importancia a su orden. Identifican a cada elemento por una clave (Key). Se escriben entre {}.

Operaciones en diccionarios:
-----------------------------

.keys():Retorna la clave de nuestro elemento.

.values(): Retorna una lista de elementos (valores del diccionario).

.items(): Devuelve lista de tuplas (primero la clave y luego el valor).

.clear(): Elimina todos los items del diccionario.

.pop(“n”): Elimina el elemento ingresado.


ENTORNO VIRTUAL
---------------

Un entorno virtual es un programa asilado que tiene sus propios modulos. Esto se hace para que si hay una actualizacion y sacan algo que nosotros usamos no se nos rompa.

Git init - inicializa un repositorio vacio de github

Al querer ingresar a python3 desde nuestra funcion si ponemos la flag -m (es un indicativo que dice que vamos a modificar el funcionamiento original. -m es el modulo interno del lenguaje) y "venv" es el modulo que significa entorno virtual. Luego de esto va el nombre que le queremos poner al entorno, generalmente se pone (venv).

Luego de hacer esto, nos va a aparecer varias carpetas adentro de nuestro entorno, nosotros vamos a tocar Script porque ahi es donde esta el comando para activar nuestro entorno virtual

Se activa con el comando : .\venv\Scripts\activate, y se deja de usar un pyton global para usar un python clonado, solamente va a funcionar en ese proyecto. Con (deactive) se sale de ese entorno.

Modulos:
-------

Un modulo es codigo escrito por otras personas que nosotros podemos utilizar, un ejemplo de modulo es Random.
En python tenemos varios modulos, que ya vienen descargados, pero hay ciertos modulos que no estan de fabrica con pythoncle y tenemos que instalarlos de manera externa, esto lo podemos hacer con un manejador de dependencias o tambien llamado instalador de paquetes. El mas popular en python es PIP (Package Installer for Python), este instalador viene de fabrica, esta pensado basicamente para instalar otros modulos que no vienen dentro de python. Un ejemplo de modulo popular externo, es pytest, que nos sirve para realizar testing. PIP es una herramienta que va acompañada con el entorno virtual y no deberiamos usarla fuera del mismo.

Usar PIP para instalar modulos en entorno virtual:
-------------------------------------------------

Lo primero que tenemos que hacer es entrar en nuestro entorno virtual, luego con el comando pip freeze veremos que modulos externos tenemos instalados.
Para instalar basicamente ponemos pip install y el nombre del modulo que nosotros queremos. Cuando instalamos modulos complejos que utilizan otros modulos, se van a instalar junto con el modulo que nosotros instalamos.

COMPARTIR PROYECTO: 

Al compartir el proyecto la otra persona debe tener el mismo python que nosotros, con los mismos modulos y todo lo que le hayamos instalado. Para eso podemos hacer pip freeze > requirements.txt, al usar este comando pasamos todos los modulos instalados a un nuevo archivo. Entonces cuando lo compartamos con otra persona, esa persona solo va a tener que escribir pip install -r requirements.txt, con esto se le instala todas las dependencias que guardamos en requirements.txt.

Datos:
------

Con random la computadora busca un valor random de lo que nosotros le aclaremos, en el caso del diccionario usamos random.choice porque lo que queremos es un caracter de cualquier tipo. Con random.randint() nos busca un numero random.

Con "code ." se abre visual desde la terminal

.gitignore: Aca ponemos el nombre del archivo que queremos ignorar cuando lo subamos a github

List comprehensions: forma de crear listas de una manera elegante simplificando el código al máximo.

Filter: filtra los datos de una lista retornando solo los que son True

Map: manipula los datos de una lista

Reduce: opera los datos de una lista entre sí para obtener 1 solo resultado

Funciones Lambdas:
------------------
Es una manera de crear funciones anonimas, sin nombre. No tienen identificacion. La estructura es "lambda argumentos: expresion" Lamda en python puede tener una sola linea de codigo, es decir una sola linea de expresion.
No es necesario escribir return porque lo hace solo


-------------------------------------------------------------

OTRO PROYECTO UWU
-----------------

FIFO (primero en entrar, primero en salir)
FILO (primero en entrar, último en salir)
LIFO (último en entrar, primero en salir)
LILO (último en entrar, último en salir)
