n = int()
num = int()
contador = int()
i = int()
esprimo = bool()
print("Ingrese la cantidad de números primos a generar: ")
n = int(input())
print("Los primeros ",n," números primos son:")
num = 2
while contador<n:
	esprimo = True
	for i in range(2,int(num/2)+1):
		if (num%i==0):
			esprimo = False
	if esprimo:
		print(num)
		contador = contador+1
	# Pasar al siguiente número
	num = num+1

