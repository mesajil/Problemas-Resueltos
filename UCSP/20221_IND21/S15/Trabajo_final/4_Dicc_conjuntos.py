"""4. Crear conjunto de palabras a partir de una oración"""


def crear_conjunto_de_palabras (oracion):
  conjunto = set()
  p = oracion.find(" ")
  while p > -1:
    conjunto.add(oracion[:p])
    oracion = oracion[p+1:]
    p = oracion.find(" ")
  conjunto.add(oracion)
  return conjunto

def crear_diccionario (f, lista):
  return {e: f(e) for e in lista} 

n = 3
contenido = []
for i in range(n):
  contenido.append(input(f"Ingrese oración {i + 1}: "))

diccionario = crear_diccionario(crear_conjunto_de_palabras, contenido)
for row in diccionario:
  print(row + ": " + str(diccionario[row]))
