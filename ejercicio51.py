import random
n = int()
i = int()
suma = int()
num = int()
num = [int() for ind0 in range(100)]
print("Ingrese el tamaño del vector: ")
n = int(input())
# Generar el vector aleatoriamente
for i in range(n):
	num[i] = random.randint(1, 20)
print("Vector = |", end="")
for i in range(n):
	print(num[i]," | ", end="")
suma = 0
for i in range(n):
	# Calcular la suma de los elementos múltiplos de 2
	if num[i]%2==0:
		suma = suma+num[i]
print("")
print("La suma de los elementos múltiplos de 2 es:",suma)

