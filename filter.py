#list comprehensions

#generar un programa que imprima los impares, por eso la condicion de %2 != 0, ya que toda numero par dividio 2 el resto es 0

#my_list = [1, 4, 5, 6, 9, 13, 19, 21]
#odd = [i for i in my_list if i %2 != 0]
#print(odd)

#para todas las i de mi lista guardo las i solo si el resultado en la divison entre 2 es diferente a 0

#uso con filter

my_list = [1,4,5,6,9,13,19,21]

odd = list(filter(lambda x: x%2 != 0, my_list))
print (odd)
