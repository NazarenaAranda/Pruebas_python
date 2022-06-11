#pasar una lista a una con los numeros elevados al cuadrado

#list comprehensions

#my_list = [1, 2, 3, 4, 5]
#cuadrado = [i**2 for i in my_list]
#print(cuadrado)

#map

my_list = [1, 2, 3, 4, 5]

cuadrado = list(map(lambda x: x**2, my_list))
print(cuadrado)