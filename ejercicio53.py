import random
a = int()
f = int()
c = int()
may = int()
pos = int()
n = int(input("ingrese la dimension de matriz: "))
a = [[int() for ind0 in range(n)] for ind1 in range(n)]
# Dimension de la matriz (fila,  columna)
for f in range(n):
	for c in range(n):
		a[f][c] = random.randint(1, 100)
may = -999999
for f in range(n):
	# aqui encontramos al elemnto mayor
	for c in range(n):
		if a[f][c]>may:
			# aqui encontramos al elemnto mayor
			may = a[f][c]
print("MATRIZ A: ")
for f in range(n):
	for c in range(n):
		if a[f][c]>9:
			print(a[f][c]," ", end="")
		else:
			print("",a[f][c]," ", end="")
	print("")
print("")
print("el numero mayor de la matriz es :",may)

