import random
n = int()
men = int()
filamenor = int()
columnamenor = int()
i = int()
j = int()
matriz = int()
n = int(input("Ingrese la dimensión de la matriz (n): "))
matriz = [[int() for ind0 in range(n)] for ind1 in range(n)]
for i in range(0,n):
	for j in range(0,n):
		matriz[i][j] = random.randint(0,100)
men = matriz[1][1]
filamenor = 1
columnamenor = 1
print("MATRIZ A: ")
for i in range(n):
	for j in range(n):
		if matriz[i][j]>9:
			print(matriz[i][j]," ", end="")
		else:
			print(" ",matriz[i][j]," ", end="")
	print("")
# Encontrar el elemento mínimo en la matriz
for i in range(n):
	for j in range(n):
		if matriz[i][j]<men:
			men = matriz[i][j]
			filamenor = i
			columnamenor = j
# Mostrar el elemento mínimo y su posición
print("El elemento mínimo es ",men," en la posición (",filamenor,",",columnamenor,").")

