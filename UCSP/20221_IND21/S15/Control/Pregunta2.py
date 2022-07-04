
"""
Ensayo con archivo:



"""
def es_divisible_por_2_y_3 (num):
  return num%2 == 0 and num%3 == 0


def intercambiar_cifras_3ra_y_4ta (num):
  cifra4 = num%10
  num = num//10
  cifra3 = num%10
  num = num//10
  return (num*10 + cifra4)*10 + cifra3


def es_numero_de_4_cifras(num):
  return num > 999


num = int(input("Numero: "))

if es_numero_de_4_cifras(num):
  if es_divisible_por_2_y_3(intercambiar_cifras_3ra_y_4ta(num)):
    print ("Es divisible por 2 y 3")
  else:
    print ("No es divisible por 2 y 3")
else:
  print ("El numero es de menos de 4 cifras")