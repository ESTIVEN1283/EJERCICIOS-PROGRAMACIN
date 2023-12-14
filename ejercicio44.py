cubo = int()
n = int(input("Ingrese un número para verificar si es un cubo perfecto: "))
cubo = 1
while cubo**3<n:
	cubo = cubo+1
if cubo**3==n:
	print(n," es un cubo perfecto.")
else:
	print(n," no es un cubo perfecto.")

