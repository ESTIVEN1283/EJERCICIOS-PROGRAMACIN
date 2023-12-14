num = int()
digito = int()
cantidadpares = int()
num = int(input("Ingrese un número: "))
cantidadpares = 0
while num>0:
	digito = num%10
	# Verificar si el dígito es par
	if digito%2==0:
		cantidadpares = cantidadpares+1
	num = int(num/10)
print("La cantidad de dígitos pares en el número es: ",cantidadpares)

