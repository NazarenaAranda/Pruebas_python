def conversacion(mensaje): #mensaje es el parametro que no se va a repetir y lo que hay adentro de la funcion es lo que se repite en cada caso
     print("Hola")
     print("Como estas")
     print(mensaje)
     print("Adios")
    

opcion = int(input("Elige una opcion (1, 2, 3): "))
if opcion == 1:
    conversacion("Elegiste la opcion 1")
elif opcion == 2:
    conversacion("Elegiste la opcion 2")
elif opcion == 3:
    conversacion("Elegiste la opcion 3")
else: 
    print("Escribe una opcion correcta")