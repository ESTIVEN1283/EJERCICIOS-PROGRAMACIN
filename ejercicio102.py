num = int()
divisor = int()
exponente = int()
num = int(input("Ingrese un número para descomponer en factores primos: "))
print("La descomposición en factores primos de ",num," es:")
divisor = 2
while num>1:
	exponente = 0
	while (num%divisor==0):
		num = int(num/divisor)
		exponente = exponente+1
	if exponente>0:
		print(divisor," ^ ",exponente)
	divisor = divisor+1

