n = int()
i = int()
num = int()
suma = int()
suma = 0
n = int(input("Ingrese la cantidad de números (N): "))
for i in range(1,n+1):
	print("Ingrese el número ",i,": ")
	num = int(input())
	suma = suma+num
print("La suma de los ",n," números ingresados es: ",suma)

