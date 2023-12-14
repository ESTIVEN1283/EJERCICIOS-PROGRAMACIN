num = int()
i = int()
num = int(input("Ingrese un número: "))
# Validar que el número sea positivo
if (num<=0):
	print("Por favor, ingrese un número positivo.")
else:
	print("Factores de ",num,":")
	# Encontrar factores
	for i in range(1,num+1):
		if (num%i==0):
			print(i)

