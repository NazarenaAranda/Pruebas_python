#con for
#multiplicar todos los valores

#my_list = [2, 2, 2, 2, 2]
#multiplicar_todo = 1

#for i in my_list:
#multiplicar_todo = multiplicar_todo * i
#print(multiplicar_todo)

#con reduce

from functools import reduce #para usar reduce la tengo que importar

my_list = [2, 2, 2, 2, 2]

multiplicar_todo = reduce(lambda a, b: a * b, my_list)
print(multiplicar_todo)