def conversor(tipo_pesos, valor_dolar): #funcion
    pesos = input("Cuantos pesos" + tipo_pesos + " tienes? ") #input es para que el usuario ingrese algo
    pesos = float(pesos) #con float pasas a decimal
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round sirve para redondear el numero los lugares que le aclaramos
    dolares = str(dolares) #str pasa el numero a texto
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 🤑

1- Pesos colombianos
2- Pesos uruguayos
3- Pesos argentinos
4- Reales

Elige una opcion: """ #las triple comillas permiten poner muchas lineas de str

opcion = int(input(menu))

if opcion == 1:
    conversor(" colombianos", 4087)
elif opcion == 2:
    conversor(" uruguayos", 41.54)
elif opcion == 3:
    conversor(" argentinos", 116.75)
elif opcion == 4:
    conversor(" brasileros", 116.75)
else:
    print("No existe esa opcion. Ingresa una opcion correcta, por favor")