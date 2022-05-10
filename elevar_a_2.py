def main():
    LIMITE = 1000000 #Esta en mayusculas porque es una variable constante, no va a cambiar en ninguna parte del codigo
    
    contador = 0
    potencia_2 = 2**contador
    
    while potencia_2 < LIMITE:
        print("2 elevado a " + str(contador) + " es igual a: " + str(potencia_2))
        contador = contador + 1
        potencia_2 = 2**contador


if __name__ == "__main__":
    main()