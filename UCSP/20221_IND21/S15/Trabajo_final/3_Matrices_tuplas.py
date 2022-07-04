"""3. Calcular el factorial de un número y guardarlo en tupla (factorial(num), num)"""


import random

def factorial(n):
	f=1
	for i in range(1,n+1):
		f=f*i
	return (f, n)

def crea_matriz (n, m):
	return [[factorial(random.randint(1,10)) for _ in range(m)] for _ in range(n)]

matriz = crea_matriz (3,3)
for row in matriz:
	print (row)