num = int()
digito = int()
digitomayor = int()
num = int(input("Ingrese un número entero: "))
# Inicializar el dígito mayor con el primer dígito del número
digitomayor = num%10
num = int(num/10)
# Proceso para encontrar el dígito mayor
while num>0:
	digito = num%10
	if digito>digitomayor:
		digitomayor = digito
	num = int(num/10)
print("El dígito mayor del número es: ",digitomayor)

