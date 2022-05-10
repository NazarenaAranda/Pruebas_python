def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Nazarena", "lastname": "Aranda"}

    super_list = [ #lista de diccionarios
        {"firstname": "Nazarena", "lastname": "Aranda"},
        {"firstname": "hola", "lastname": "pepito"},
        {"firstname": "anoche", "lastname": "fui"},
        {"firstname": "a un", "lastname": "baile"},
        {"firstname": "juajua", "lastname": "jeje"},
    ]


    super_dict = { #diccionario de listas
        "natural_nums": [1, 2, 2, 3, 4],
        "integer_nums": [-1, -2, -3, 0],
        "floating_nums": [1.1, 2.7, 2.53]
    }

    #for key, value in super_dict.items(): #imprimir el super_dictionario
        #print(key, "-", value)

    for list in super_list: #imprimir super_lista
        print(list)

if __name__ == "__main__":
    main()