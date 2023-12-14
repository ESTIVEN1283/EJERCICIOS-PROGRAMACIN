import random
cantidadnumeros = int()
num = int()
contadormultiplos3 = int()
contadormultiplos4 = int()
i = int()
cantidadnumeros = int(input("Ingrese la cantidad de números en la lista: "))
contadormultiplos3 = 0
contadormultiplos4 = 0
for i in range(1,cantidadnumeros+1):
	# Generar un número aleatorio entre 1 y 100
	num = random.randint(1, 100)
	print("Número generado: ",num)
	# Verificar si es múltiplo de 3
	if num%3==0:
		print("Es múltiplo de 3.")
		contadormultiplos3 = contadormultiplos3+1
	# Verificar si es múltiplo de 4
	if num%4==0:
		print("Es múltiplo de 4.")
		contadormultiplos4 = contadormultiplos4+1
	print("")
print("Cantidad de números múltiplos de 3: ",contadormultiplos3)
print("Cantidad de números múltiplos de 4: ",contadormultiplos4)
