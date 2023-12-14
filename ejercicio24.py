contador = int()
num = int()
suma = int()
n = int(input("Ingrese el valor de N:"))
contador = 0
suma = 0
while contador<n:
	num = int(input("Ingrese un número:"))
	if num%3==0:
		suma = suma+num
		contador = contador+1
print("La suma de los primeros ",n," términos múltiplos de 3 es: ",suma)

