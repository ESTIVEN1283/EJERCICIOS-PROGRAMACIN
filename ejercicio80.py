num = int()
contador = int()
num = int(input("Ingrese un número: "))
contador = 0
while num!=0:
	num = int(num/10)
	contador = contador+1
print("El número tiene ",contador," dígitos.")

