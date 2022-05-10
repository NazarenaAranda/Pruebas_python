def palindromo(palabra):
    palabra = palabra.replace(' ', '') #saca los espacios
    palabra = palabra.lower() #minimiza toda la palabra
    palabra_invertida = palabra[::-1] #va de principio a fin pero al reves, por eso el menos 1
    if palabra == palabra_invertida:
        return True
    else:
        return False

def main(): #funcion principal, va a correr todo el programa desde el inicio al final
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")


if __name__ == "__main__": #punto de entrada
    main()