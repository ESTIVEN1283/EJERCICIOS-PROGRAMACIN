may = float()
men = float()
medio = float()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
# Encontrar el número mayor
if num1>=num2 and num1>=num3:
	may = num1
else:
	if num2>=num1 and num2>=num3:
		may = num2
	else:
		may = num3
# Encontrar el número menor
if num1<=num2 and num1<=num3:
	men = num1
else:
	if num2<=num1 and num2<=num3:
		men = num2
	else:
		men = num3
# Encontrar el número del medio
if (num1!=may and num1!=men):
	medio = num1
else:
	if (num2!=may and num2!=men):
		medio = num2
	else:
		medio = num3
print("El número medio es: ",men)
