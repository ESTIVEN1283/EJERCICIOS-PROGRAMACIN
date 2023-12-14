num = int()
i = int()
esprimo = int()
num = int(input("Ingrese un número entero positivo mayor que 1: "))
esprimo = 1
# Verificar si el número es primo
if num<=1:
	esprimo = 0
else:
	for i in range(2,int(num/2)+1):
		if num%i==0:
			esprimo = 0
if esprimo==1:
	print("El número ",num," es primo.")
else:
	print("El número ",num," no es primo.")
