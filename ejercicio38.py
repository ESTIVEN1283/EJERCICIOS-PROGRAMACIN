a = int()
f = int()
c = int()
a = [[int() for ind0 in range(5)] for ind1 in range(5)]
# Dimension de la matriz (fila,  columna)
# genra una matriz - entrada
for f in range(5):
	for c in range(5):
		a[f][c] = f+1+c
# muestra datos de la matriz - salida
print("MATRIZ A: ")
for f in range(5):
	for c in range(5):
		if a[f][c]>9:
			print(a[f][c]+1," ", end="")
		else:
			print(" ",a[f][c]+1," ", end="")
	print(" ")
