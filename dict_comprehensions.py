def main():
    #my_dict = {}
 
    #for i in range(1, 101): #codigo normal
        #if i % 3 != 0:
            #my_dict[i] = i**3

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0} #diccionario comprehensions. La diferencia que tiene con las listas ademas de los corchetes es que en los diccionarios al principio le tenemos que dar una llave y luego el valor
    print(my_dict)

if __name__ == "__main__":
    main()