import random
i = int()
j = int()
dim = int()
v = int()
dim = int(input("ingrese la dimension para el vector: "))
# DIMENSION INGRESADO POR TECLADO
v = [int() for ind0 in range(dim)]
i = [int() for ind0 in range(dim)]
for j in range(dim):
	v[j] = random.randint(16, 55)
for j in range(dim-1,-1,-1):
	i[(dim-1)-j] = v[j]
print("")
print("v = | ", end="")
for j in range(dim):
	print(v[j]," | ", end="")
print("")
print("vertor invertido")
print("v = | ", end="")
for j in range(dim):
	print(i[j]," | ", end="")
print("")

