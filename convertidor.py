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