print ("Hello World!")
my_var = None
print (my_var)
print (type (my_var))

# Strings
cad1 = "Hello "
cad2 = "World!"
print (cad1 + cad2) # Concatenación
print (len(cad1 + cad2)) # Longitud

# Slicing
cad = cad1 + cad2
print (cad[0]) # Primer caracter
print (cad[-1]) # Ultimo caracter
print (cad[5:]) # Rebanada
print (cad[::-1]) # Invertir cadena

# Código Ascii
car = "A"
print (ord(car)) # CHAR -> ASCII
print (chr(65)) # ASCII -> CHAR
print (chr(ord(car) + 5)) # CHAR -> CHAR

