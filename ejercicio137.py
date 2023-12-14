num = int()
sumadigitos = int()
num = int(input("Ingrese un número: "))
sumadigitos = 0
while sumadigitos>=10:
	sumadigitos = 0
	# Sumar los dígitos del número
	while num>0:
		sumadigitos = sumadigitos+num%10
		num = int(num/10)
		print("La suma de los dígitos es: ",sumadigitos)
print("La suma final de los dígitos es menor a 10.")

