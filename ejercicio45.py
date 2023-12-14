n = int()
suma = int()
i = int()
n = int(input("Ingrese un número N: "))
suma = 0
for i in range(n+1):
	if i>=0:
		suma = suma+i
print("La suma de los términos no negativos hasta ",n," es: ",suma)

