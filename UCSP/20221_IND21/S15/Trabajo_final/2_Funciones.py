"""2. Calcular numero de vocales en un parrafo y sus respectivas cantidades por cada vocal"""


def numero_vocales(cadena):
  vocales = [[0, c] for c in "aeiou"]
  for c in cadena:
    for p in vocales:
      if c.lower() == p[1]:
        p[0] += 1
  return [(n, c) for n,c in vocales]

def aplicar_funcion (f, lista):
  return [(f(e), e) for e in lista]


contenido = ["Erase una vez ...", "Dumbledore dijo que ..."]

for row in aplicar_funcion(numero_vocales, contenido):
  print (row)