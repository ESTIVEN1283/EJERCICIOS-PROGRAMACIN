num1 = float()
num2 = float()
num3 = float()
mayor = float()
menor = float()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
if num1>=num2 and num1>=num3:
	mayor = num1
else:
	if num2>=num1 and num2>=num3:
		mayor = num2
	else:
		mayor = num3
if num1<=num2 and num1<=num3:
	menor = num1
else:
	if num2<=num1 and num2<=num3:
		menor = num2
	else:
		menor = num3
print("El número mayor es: ",mayor)
print("El número menor es: ",menor)

