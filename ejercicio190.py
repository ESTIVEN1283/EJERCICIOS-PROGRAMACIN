num = int()
digito = int()
sumaimpares = int()
print("Ingrese un número: ")
num = int(input())
sumaimpares = 0
while num>0:
	digito = num%10
	# Verificar si el dígito es impar
	if digito%2!=0:
		sumaimpares = sumaimpares+digito
	num = int(num/10)
print("La suma de los dígitos impares es: ",sumaimpares)

