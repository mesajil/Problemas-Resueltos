

"""1. Crear clase Libro, crear el método "agregar_parrafo" y
utilizar el método __str__ para imprimir su contenido"""
class Libro():
  def __init__ (self, titulo):
    self.titulo = titulo
    self.contenido = []
  
  def agregar_parrafo (self, parrafo):
    self.contenido.append(parrafo)
  
  def agregar_muchos_parrafos (self, lista):
    self.contenido.extend(lista)

  def __str__ (self):
    imprimir = self.titulo + "\n\n"
    for p in self.contenido:
      imprimir += p + "\n"
    return imprimir

mi_libro = Libro("Harry Potter")
mi_libro.agregar_parrafo("Erase una vez ...")
mi_libro.agregar_parrafo("Dumbledore dijo que ...")
mi_libro.agregar_muchos_parrafos(["Entonces Lord Voldemort empezó lo que sería ...", "Por fin, Harry logró recuperar la piedra que ..."])
print(mi_libro)