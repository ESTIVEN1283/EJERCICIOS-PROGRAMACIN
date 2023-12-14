c = int()
contador = int()
c = int(input("ingrese un  numero: "))
while c<=100:
	if (c%7!=0) and (c%9!=0):
		print(" ",c, end="")
	c = c+1

