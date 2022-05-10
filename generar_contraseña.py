import random
from re import S

def generar_contrasena():
    Mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    Minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    Num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    Simbolos = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']

    caracteres = Mayus + Minus + Num + Simbolos

    contrasena = []

    for i in range(15): #queremos que nuestra contraseña tenga 15 caracteres
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random) #con append agregamos a contrasena caracter_random
        
    contrasena = "".join(contrasena) #join convierte todo a string y le saca los espacios
    return contrasena

def main():
    contrasena = generar_contrasena()
    print("Tu nueva contraseña es: " + contrasena)

if __name__ == "__main__":
    main()