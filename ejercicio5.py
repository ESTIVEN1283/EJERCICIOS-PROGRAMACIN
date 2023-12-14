cociente = int()
residuo = int()
dividendo = int(input("Ingrese el dividendo: "))
divisor = int(input("Ingrese el divisor: "))
cociente = 0
residuo = dividendo
while residuo>=divisor:
	residuo = residuo-divisor
	cociente = cociente+1
print("El cociente es: ",cociente)
print("El residuo es: ",residuo)

