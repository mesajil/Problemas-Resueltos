

"""
Ensayo con archivo:



Solución:

Codifique un programa que cree una clase Extraterrestre, que tenga como atributos
el radio de su planeta natal en kilómetros y la distancia con respecto al sol (en años luz).
La clase tendrá el método "respuesta", que retorna un string que modifica el mensaje de la
siguiente manera.

Para el mensaje = "Hola", el método retorna "aloHaloHaloH ..."
Es decir retorna el mensaje con las caracteres invertidos y multiplicado tantas
veces como su "distancia" entre su "radio".
Debe redondear si la división anterior no es entera.
"""

class Extraterrestre:
  def __init__ (self, radio, distancia):
    self.radio = radio
    self.distancia = distancia
  
  def respuesta (self, mensaje):
    return (mensaje[::-1])*int(self.distancia/self.radio)


e1 = Extraterrestre(20000, 300000)
print (e1.respuesta("Hola"))