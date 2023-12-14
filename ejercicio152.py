num = int()
suma = int()
digito = int()
print("Ingrese un número:")
num = int(input())
suma = 0
while num>0:
	digito = num%10
	suma = suma+digito
	num = int(num/10)
print("La suma de los dígitos es:",suma)

