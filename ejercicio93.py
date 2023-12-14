num = int()
dig = int()
inv = int()
num = int(input("Ingrese un número entre 10 y 100: "))
if ((num>10) and (num<100)):
	inv = 0
	while (num>0):
		dig = num%10
		inv = inv*10+dig
		num = int(num/10)
	print("El número invertido es: ",inv)
else:
	print("No se puede imprimir ")

