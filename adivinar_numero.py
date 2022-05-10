import random

def main():

    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input("elige un numero del 1 al 100: "))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print("Piensa en un numero mas grande")
            numero_elegido = int(input("elige otro numero: "))
        else:
            print("Piensa en un numero mas pequeño")
            numero_elegido = int(input("elige otro numero: "))
    print("Ganaste!!")  
 

if __name__ == "__main__":
    main()