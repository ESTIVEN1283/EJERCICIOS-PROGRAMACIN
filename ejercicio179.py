num = int()
numerooriginal = int()
numeroinvertido = int()
digito = int()
print("Ingrese un número: ")
num = int(input())
numerooriginal = num
numeroinvertido = 0
while (num>0):
	digito = num%10
	numeroinvertido = numeroinvertido*10+digito
	num = int(num/10)
if (numerooriginal==numeroinvertido):
	print("El número ",numerooriginal," es capicúa.")
else:
	print("El número ",numerooriginal," NO es capicúa.")

