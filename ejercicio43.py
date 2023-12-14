import random
a = int()
v = int()
i = int()
j = int()
suma = int()
sum = int()
res = int()

dim = int(input("ingrese la dimension de los vectores: "))
a = [int() for ind0 in range(dim)]
v = [int() for ind0 in range(dim)]
for i in range(dim):
	# llenado del A
	a[i] = random.randint(1, 9)
suma = 0
for i in range(dim):
	suma = suma+a[i]
for j in range(dim):
	# llenado del v
	v[j] = random.randint(1, 5)
sum = 0
for j in range(dim):
	sum = sum+v[j]
# salida de los elemntos del A - SALIDA
print("A =|", end="")
for i in range(dim):
	print(a[i]," | ", end="")
print("")
# salida de los elemntos del v - SALIDA
print("v =|", end="")
for j in range(dim):
	print(v[j]," | ", end="")
print("")
res = suma+sum
print("suma A = ",suma)
print("suma v = ",sum)
print("la suma de los dos vectores es: ",res)
