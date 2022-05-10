menu = """ 
Bienvenido al conversor de monedas 🤑

1- Pesos colombianos
2- Pesos uruguayos
3- Pesos argentinos
4- Reales

Elige una opcion: """ #las triple comillas permiten poner muchas lineas de str

opcion = int(input(menu))

if opcion == 1:
    pesos = input("Cuantos pesos colombianos tienes?" ) #input es para que el usuario ingrese algo
    pesos = float(pesos) #con float pasas a decimal
    valor_dolar = 4087
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round sirve para redondear el numero los lugares que le aclaramos
    dolares = str(dolares) #str pasa el numero a texto
    print("Tienes $" + dolares + " dolares")
    
    dolares = input("Cuantos dolares tienes?" )
    dolares = float(dolares)
    valor_pesos = 0.00025
    pesos = dolares / valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " pesos colombianos")

elif opcion == 2:
    pesos = input("Cuantos pesos uruguayos tienes?" ) #input es para que el usuario ingrese algo
    pesos = float(pesos) #con float pasas a decimal
    valor_dolar = 41.54
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round sirve para redondear el numero los lugares que le aclaramos
    dolares = str(dolares) #str pasa el numero a texto
    print("Tienes $" + dolares + " dolares")
    
    dolares = input("Cuantos dolares tienes?" )
    dolares = float(dolares)
    valor_pesos = 0.024
    pesos = dolares / valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " pesos uruguayos")

elif opcion == 3:
    pesos = input("Cuantos pesos argentinos tienes?" ) #input es para que el usuario ingrese algo
    pesos = float(pesos) #con float pasas a decimal
    valor_dolar = 116.75
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round sirve para redondear el numero los lugares que le aclaramos
    dolares = str(dolares) #str pasa el numero a texto
    print("Tienes $" + dolares + " dolares")
    
    dolares = input("Cuantos dolares tienes?" )
    dolares = float(dolares)
    valor_pesos = 0.0086
    pesos = dolares / valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " pesos argentinos")

elif opcion == 4:
    pesos = input("Cuantos reales tienes?" ) #input es para que el usuario ingrese algo
    pesos = float(pesos) #con float pasas a decimal
    valor_dolar = 5.16
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) #round sirve para redondear el numero los lugares que le aclaramos
    dolares = str(dolares) #str pasa el numero a texto
    print("Tienes $" + dolares + " dolares")
    
    dolares = input("Cuantos reales para pasar a pesos uruguayos?")
    dolares = float(dolares)
    valor_pesos = 8.05
    pesos = dolares / valor_pesos
    pesos = round(pesos, 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " pesos uruguayos")

else:
    print("No existe esa opcion. Ingresa una opcion correcta, por favor")