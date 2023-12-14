import random
v = int()
i = int()
j = int()
aux = int()
dim = int()
dim = int(input("INGRESE LA DIMENCION DEL VECTOR: "))
v = [int() for ind0 in range(dim)]
for i in range(dim):
	v[i] = random.randint(1, 6)
print("VECTOR ORIGINAL")
print(" V = | ", end="")
for i in range(dim):
	print(v[i]," | ", end="")
print("")
for i in range(1,dim):
	for j in range(dim-1):
		if v[j]<v[j+1]:
			aux = v[j]
			v[j] = v[j+1]
			v[j+1] = aux
print(" ")
print("VECTOR ORDENADO ")
print(" V = | ", end="")
for i in range(dim-1,-1,-1):
	print(v[i]," | ", end="")
print(" ")

