def main():

    cuadrado = [ i for i in range(1,1000) if i % 36 == 0 #36 es el numero multiplo de 4, 6 y 9
]
    print(cuadrado) #La linea de arriba se lee "para cada i en el rango del 1 al 1000, lo guardo en i solamente si al dividir con 36 el resto es 0"

#esto es list comprehensions

if __name__ == "__main__":
    main()