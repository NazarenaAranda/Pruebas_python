pesos = input("Cuantos pesos Colombianos tienes?" )
pesos = float(pesos)
valor_dolar = 4087
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")