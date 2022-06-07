#def palindromo(string):
    #return string == string[::-1] #codigo con una funcion normal
#print(palindromo("ana"))

palindromo = lambda string: string == string[::-1] #codigo con lambda
print(palindromo("ana"))
#"palindromo" - identificador
# "lambda string" - argumento
#"string == string[::-1]" - expresión

#lambda argumentos: expresión - Se usa lamdba en vez de def y en python esta funcion es una sola linea de codigo