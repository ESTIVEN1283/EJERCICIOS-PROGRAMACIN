n = int()
x = int()
n = int(input(" ingresa un numero: "))
x = 1
while x<=n:
	if n%x==0:#para saber si es divisor o no
		print(" El numero ",n," es divisor  con ",x)
	x = x+1
