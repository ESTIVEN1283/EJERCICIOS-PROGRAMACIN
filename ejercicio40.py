f = int()
c = int()
dim = int()
dim = int(input("ingrese la dimension de la matriz: "))
for f in range(dim):
	for c in range(dim):
		# triangular superior (f>=c triangular inferior)
		if f>=c:
			print(1," ", end="")
		else:
			print(0," ", end="")
	print("")

