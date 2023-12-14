f = int()
c = int()
dim = int()
dim = int(input("imgrese la dimension de la matriz: "))
for f in range(dim):
	for c in range(dim):
		# f = 0 primera fila f = dim-1 ultima fila
		# doagonal principal f=c
		# diagonal secundaria (f + c = dim-1)
		if f==c or (f+c==dim-1):
			print(dim," ", end="")
		else:
			print(0," ", end="")
	print("")

