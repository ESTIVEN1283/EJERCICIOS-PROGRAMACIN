num = int()
factor = int()
num = int(input("Ingrese un número entero positivo mayor que 1: "))
# Validar que el número sea mayor que 1
if num<=1:
	print("Por favor, ingrese un número mayor que 1.")
else:
	# Encuentra y muestra los factores primos
	factor = 2
	# Comienza con el primer número primo
	print("Los factores primos de ",num," son: ")
	while num>1:
		while num%factor==0:
			# El factor encontrado es primo
			print(factor)
			num = int(num/factor)
		factor = factor+1

