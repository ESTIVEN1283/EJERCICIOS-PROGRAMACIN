import random
num = int()
contadorpositivos = int()
contadornegativos = int()
contadorceros = int()
i = int()
contadorpositivos = 0
contadornegativos = 0
contadorceros = 0
for i in range(1,11):
	# Generar un número aleatorio entre -100 y 100
	num = random.randint(-4, 10)
	print("Número generado: ",num)
	# Contar positivos, negativos o ceros
	if num>0:
		contadorpositivos = contadorpositivos+1
	else:
		if num<0:
			contadornegativos = contadornegativos+1
		else:
			contadorceros = contadorceros+1
	print("")
	# Espacio en blanco para separar los números generados
print("Cantidad de números positivos: ",contadorpositivos)
print("Cantidad de números negativos: ",contadornegativos)
print("Cantidad de ceros: ",contadorceros)

