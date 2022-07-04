"""5. Calcule el numero de palabras en un parrafo"""


def calcular_numero_de_palabras_por_cada_elemento (lista):
  salida = []
  for e in lista:
    spaces = 0
    for c in e:
      if c == " ":
        spaces += 1
    salida.append((spaces + 1, e))
  return salida

def multiplicar (a,b):
  return a*b

n = 3
contenido = []
for i in range(n):
  contenido.append(input(f"Ingrese oración {i + 1}: "))

for cantidad, cadena in calcular_numero_de_palabras_por_cada_elemento(contenido):
  print(f"{cantidad} x {cadena} = {multiplicar(cantidad, cadena)}")