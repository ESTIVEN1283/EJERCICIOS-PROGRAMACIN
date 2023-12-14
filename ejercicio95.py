num = int()
digito1 = int()
digito2 = int()
digito3 = int()
sumdigitos = int()
while True:# no hay 'repetir' en python
	num = int(input("Ingrese un número de tres cifras: "))
	if num<=999 and num>=100: break
digito1 = int(num/100)
digito2 = int((num/10))%10
digito3 = num%10
sumdigitos = digito1+digito2+digito3
print("La suma de los dígitos es: ",sumdigitos)

