num1 = float()
num2 = float()
num3 = float()
medio = float()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Verificar si los números son iguales
if num1==num2 and num2==num3:
	print("Los números son iguales.")
else:
	# Encontrar el número del medio
	if (num1>=num2 and num1<=num3) or (num1<=num2 and num1>=num3):
		medio = num1
	else:
		if (num2>=num1 and num2<=num3) or (num2<=num1 and num2>=num3):
			medio = num2
		else:
			medio = num3
	# Mostrar el número del medio
	print("El número del medio es: ",medio)
