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

# Manejo de caracteres Ascii
print (ord("A")) # CHAR -> ASCII
print (chr(65)) # ASCII -> CHAR
print (chr(ord("A") + 5)) # CHAR -> CHAR

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


# Tuples: La tupla es una lista ordenada e inmatuble de datos 
t = () # tupla vacía
print (t)
t = 1, # tupla de un elemento
print (t)
t = 5, "Hello", 77 # tupla de varios elementos. También se pueden usar parentesis.
print (t)
t = tuple([1,2,3,4]) # list -> tuple
print (t)
l = list((1,)) # tuple -> list
print (l)


# Sets: Un conjunto es una colección no ordenada objetos únicos. Los objetos son no mutables.
s = {1, "Hello", False, (1,)} 
print (f"{s} es un set")
s = set() # Conjunto vacío
print (s)
s = set([1,2,2,3]) # list -> set
print (s)
s.add(4) # Añadir elemento
s.discard(1) # Descartar elemento. discard() lanzará excepción si no encuentra el elemento.
print (s)
print (2 in s) # Validar elemento
s.clear() # Descartar todos los elementos
print (s)
s = {1,2,3,4,5}
print (s.pop()) # Descartar elemento aleatorio. Error si el set está vacío
print (s)
print ({1, 2} | {2, 3}) # Unión de conjuntos
print ({1, 2} & {2, 3}) # Intersección de conjuntos
print ({1, 2} - {2, 3}) # Diferencia de conjuntos
print ({"Hello", 2} == {2, "Hello"}) # Igualdad de conjuntos
print ({3,4}.symmetric_difference({4,5})) # Diferencia simétrica. También: ^
print ({3}.issubset({2,3})) # Validar si un conjunto es subconjunto de otro. También: <=
print ({1,2,3}.issuperset({3,4})) # Validar si un conjunto es superconjunto de otro. También: >=
print ({1,2}.isdisjoint({2,3})) # Dos conjuntos son disjuntos si la interseción es el conjunto vacío
print (frozenset({1,2,3})) # Conjunto inmutable


# Diccionarios

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

