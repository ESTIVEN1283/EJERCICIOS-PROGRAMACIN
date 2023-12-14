limite = float()
terminoactual = float()
print("Ingrese un número límite: ")
limite = float(input())
print("La serie de potencias de dos hasta que el término sea menor a ",limite," es:")
terminoactual = 2
while terminoactual<limite:
	terminoactual = terminoactual*2
	print(" ",terminoactual," ", end="")

