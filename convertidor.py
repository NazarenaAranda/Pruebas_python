pesos = input("Cuantos pesos uruguayos tienes?" )
pesos = float(pesos)
valor_dolar = 41.54
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Tienes $" + dolares + " dolares")

dolares = input("Cuantos dolares tienes?" )
dolares = float(dolares)
valor_pesos = 0.024
pesos = dolares / valor_pesos
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos uruguayos")