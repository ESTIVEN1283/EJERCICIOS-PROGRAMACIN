num1 = float()
num2 = float()
resultado = float()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
if num1==num2:
	# Multiplicar si son iguales
	resultado = num1*num2
	print("Los números son iguales. La multiplicación es: ",resultado)
else:
	if num1>num2:
		# Dividir mediante restas sucesivas si el primero es mayor
		resultado = 0
		while num1>=num2:
			num1 = num1-num2
			resultado = resultado+1
		print("El primer número es mayor. La división es: ",resultado)
	else:
		# Sumar si el segundo es mayor
		resultado = num1+num2
		print("El segundo número es mayor. La suma es: ",resultado)
