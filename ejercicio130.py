num = int()
digito = int()
print("Ingrese un número: ")
num = int(input())
print("Los dígitos del número en orden inverso son:")
while num>0:
	digito = num%10
	print(digito,"", end="")
	num = int(num/10)
print("")
