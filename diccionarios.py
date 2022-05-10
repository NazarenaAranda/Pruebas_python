def main():
    mi_diccionario = {
        "llave1": 1, #son llaves que contienen un valor determinado
        "llave2": 2,
        "llave3": 3,
    }
    #print(mi_diccionario) #esto me va a imprimir lo que hay dentro del diccionario incluyendo las llaves y sus valores
    #print(mi_diccionario["llave1"]) #solo imprime el valor de esa llave
    #print(mi_diccionario["llave2"])
    #print(mi_diccionario["llave3"])

    #for llave in mi_diccionario.keys(): #con keys lo que hace es imprimir solo el nombre de las llaves
        #print(llave) #imprime las llaves

     #for llave in mi_diccionario.values(): #imprime solo el valor de las llaves que hay en el diccionario
         #print(llave)

    for llave, valor in mi_diccionario.items(): #con items imprimo todo, como son 2 items diferentes, es decir el nombre de la llave y el valor. tengo que poner algo que identifique al primer item(llave) y algo que identifique al segundo(valor)
        print(llave + " Es la llave " + str( valor)) #pongo str porque estoy convirtiendo el numero en string, porque no se pueden concatenar dos tipos diferentes


if __name__ == "__main__":
    main()
