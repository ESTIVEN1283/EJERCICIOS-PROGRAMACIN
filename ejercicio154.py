n = int()
i = int()
# Entrada de datos
print("Ingrese un número entero mayor que 0: ")
n = int(input())
if n<=0:
	print("Por favor, ingrese un número mayor que 0.")
else:
	# Mostrar los divisores de n
	print("Los divisores de ",n," son:")
	for i in range(1,n+1):
		if n%i==0:
			print(i)
