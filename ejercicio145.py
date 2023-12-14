numero1 = int()
numero2 = int()
sumapar = int()
print("Ingresar el primer número par: ")
numero1 = int(input())
print("ingresar el segundo numero par:")
numero2 = int(input())
if numero1%2==0 and numero2%2==0:
	sumapar = numero1+numero2
	print("suma = ",sumapar)
else:
	print("los numeros ingresados no son pares ")
