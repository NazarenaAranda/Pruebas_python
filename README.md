Concepts of functions that come inside the python program:
--------------------------------------------------------------

.upper() - Convert all text to uppercase

.capitalize() - Convert the first letter to uppercase

.strip() - Delete junk spaces

.replace() - replace the first parameter we give it inside the parenthesis with the second one

len - See how many characters a string has

.append() - Add an element to a list

.pop() - delete items from a list

round(name of what we want to round, x) - Round the number x from the places that we clear it

Lists and Tuples:
--------------

In python in comparison to C, inside a list(array), I can have different elements of different types, that is to say, I can put a character, a string, an integer, etc.

Lists are dynamic, take more memory, and [] is used. On the other hand, the tuples are static, that means that I can not use append or pop, being static they occupy less memory and are identified with ().

The tuples are immutable (they cannot change), as well as the strings. Lists are mutable (they can change). That's the difference they have

Python dictionaries are a mutable data structure which store different types of values without giving importance to their order. They identify each element by a key. They are written between {}.

Operations on dictionaries:
-----------------------------

.keys():Returns the key of our element.

.values(): Returns a list of items (dictionary values).

.items(): Returns list of tuples (first the key and then the value).

.clear(): Removes all items from the dictionary.

.pop("n"): Removes the entered item.


VIRTUAL ENVIRONMENT
---------------

A virtual environment is an isolated program that has its own modules. This is done so that if there is an update and they release something that we use, it won't break.

Git init - initialize an empty github repository

When we want to enter python3 from our function if we set the -m flag (it is a flag that says that we are going to modify the original operation. -m is the internal module of the language) and "venv" is the module that means virtual environment. After this goes the name that we want to put to the environment, generally it is put (venv).

After doing this, we will see several folders inside our environment, we are going to touch Script because that is where the command to activate our virtual environment is located

It is activated with the command : .\venv\Scripts\activate, and we stop using a global pyton to use a cloned python, it will only work in that project. With (deactivate) you exit that environment.

Modules:
-------

A module is code written by other people that we can use, an example of a module is Random.
In python we have several modules, which are already downloaded, but there are certain modules that are not factory with pythoncle and we have to install them externally, this can be done with a dependency manager or also called package installer. The most popular in python is PIP (Package Installer for Python), this installer comes from factory, it is basically intended to install other modules that do not come with python. An example of a popular external module is pytest, which is used for testing. PIP is a tool that comes with the virtual environment and should not be used outside of it.

Use PIP to install modules in virtual environment:
-------------------------------------------------

The first thing we have to do is to enter in our virtual environment, then with the command pip freeze we will see which external modules we have installed.
To install basically we put pip install and the name of the module we want. When we install complex modules that use other modules, they are going to be installed along with the module that we install.

SHARE PROJECT: 
-----------------

When sharing the project the other person must have the same python as us, with the same modules and everything we have installed. For that we can do pip freeze > requirements.txt, using this command we pass all the installed modules to a new file. Then when we share it with another person, that person is just going to have to type pip install -r requirements.txt, with this it installs all the dependencies we saved in requirements.txt.

Data:
------

With random the computer looks for a random value of what we clarify to him, in the case of the dictionary we use random.choice because what we want is a character of any type. With random.randint() it looks for a random number.

With "code ." it is opened visual from the terminal

.gitignore: Here we put the name of the file that we want to ignore when we upload it to github.

List comprehensions: way to create lists in an elegant way simplifying the code to the maximum.

![1_DreeF8a4h2pvxRly39HjAA](https://user-images.githubusercontent.com/98347450/173175518-16178b30-1c64-4284-8dca-96cbf15576bb.jpeg)

Map: manipulates the data of a list, the output has the same amount of values as the input.

Filter: filters the data of a list returning only those that are True or False according to the value that is within the searched criteria or not.

Reduce takes 2 values given as parameters and the iterator as another parameter. It performs the function with these 2 values, and then with the result of this and the value that follows it in the array. And so on until it goes through all the values in the list.

Lambda functions:
------------------
It is a way to create anonymous functions, without name. They have no identification. The structure is "lambda arguments: expression" Lamda in python can have a single line of code, that is a single line of expression.
It is not necessary to write return because it does it by itself.



---------------------------------------------------------------



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
-----------------

Al compartir el proyecto la otra persona debe tener el mismo python que nosotros, con los mismos modulos y todo lo que le hayamos instalado. Para eso podemos hacer pip freeze > requirements.txt, al usar este comando pasamos todos los modulos instalados a un nuevo archivo. Entonces cuando lo compartamos con otra persona, esa persona solo va a tener que escribir pip install -r requirements.txt, con esto se le instala todas las dependencias que guardamos en requirements.txt.

Datos:
------

Con random la computadora busca un valor random de lo que nosotros le aclaremos, en el caso del diccionario usamos random.choice porque lo que queremos es un caracter de cualquier tipo. Con random.randint() nos busca un numero random.

Con "code ." se abre visual desde la terminal

.gitignore: Aca ponemos el nombre del archivo que queremos ignorar cuando lo subamos a github

List comprehensions: forma de crear listas de una manera elegante simplificando el código al máximo.

![1_DreeF8a4h2pvxRly39HjAA](https://user-images.githubusercontent.com/98347450/173175518-16178b30-1c64-4284-8dca-96cbf15576bb.jpeg)

Map: manipula los datos de una lista, el output tiene la misma cantidad de valores que el input

Filter: filtra los datos de una lista retornando solo los que son True o False según el valor que esté dentro de los criterios buscados o no

Reduce toma 2 valores entregados como parámetros y el iterador como otro parámetro. Realiza la función con estos 2 valores, y luego con el resultado de esto y el valor que le sigue en el array. Y así hasta pasar por todos los valores de la lista.

Funciones Lambda:
------------------
Es una manera de crear funciones anonimas, sin nombre. No tienen identificacion. La estructura es "lambda argumentos: expresion" Lamda en python puede tener una sola linea de codigo, es decir una sola linea de expresion.
No es necesario escribir return porque lo hace solo.

Función de orden superior:
---------------------------
Es una función que recibe como parámetro a otra función
