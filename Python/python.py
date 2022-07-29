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
print (cad[::-1]) # Retorna cadena invertida
print (cad)

# Código Ascii
car = "A"
print (ord(car)) # CHAR -> ASCII
print (chr(65)) # ASCII -> CHAR
print (chr(ord(car) + 5)) # CHAR -> CHAR

# Listas
l = ["Hello ", "World!", 1, 2]
print (l[0] + l[1]) # Slicing
l[2] = 500 # Cambiar valores
print (l)
del l[2] # Eliminar elemento por índice. También: del l[:]; del l[], l[]
l.remove("World!") # Buscar y eleminar elemento dado
print (l.pop(-1)) # Eliminar elemento por índice y retornarlo
print (l)
l += ["World!"] # Agregar elemento versión 1
l.append(77) # Agregar elemento versión 2 
print (l)
l.extend([5, 6, 7]) # Extender una lista de elementos dado
print (l)
l.insert(-3, 4) # Insertar elemento (posición, elemento)
print (l.index(77)) # Ver índice de un elemento
print ("Hello " in l) # Validar elemento en una lista
print (l.count(7)) # Contar número de elementos para un valor dado
print (l[::-1]) # Retorna lista invertida
l.reverse() # Invertir lista
print (l)
del l[-2:]
print (l)
l.sort() # Ordenar lista de menor a mayor (elementos del mismo tipo)
print (l)
l.sort(reverse=True) # Ordenar lista de mayor a menor (elementos del mismo tipo)
print (l)


t = () # La tupla es una lista ordenada e inmatuble de datos
print (t) # tupla vacía
t = 1, # tupla de un elemento
print (t)
t = 5, "Hola", 77 # tupla de varios elementos. También se pueden usar parentesis.
print (t)
t = tuple([1,2,3,4]) # list -> tuple
print (t)
l = list((1,)) # tuple -> list
print (l)


