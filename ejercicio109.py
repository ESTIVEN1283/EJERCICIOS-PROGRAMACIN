num = int()
sumadivisores = int()
i = int()
esprimo = bool()
esperfecto = bool()
num = int(input("Ingrese un número: "))
# Verificar si el número es primo
esprimo = True#verdadero
for i in range(2,int(num/2)+1):
	if (num%i==0):
		esprimo = False#falso
# Verificar si el número es perfecto
sumadivisores = 1
for i in range(2,int(num/2)+1):
	if (num%i==0):
		sumadivisores = sumadivisores+i
esperfecto = (num==sumadivisores)
if esprimo:
	print("El número ingresado es primo.")
else:
	print("El número ingresado no es primo.")
if esperfecto:
	print("El número ingresado es perfecto.")
else:
	print("El número ingresado no es perfecto.")

