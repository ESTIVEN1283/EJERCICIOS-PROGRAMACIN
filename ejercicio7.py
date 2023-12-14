from math import sqrt#librearia de math y raiz
num = int()
res = int()
print("Ingrese un número: ")
num = int(input())
res = round(sqrt(num))
if (res*res)==num:
	print("El número es un cuadrado perfecto.")
else:
	print("El número NO es un cuadrado perfecto.")

