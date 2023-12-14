resultado = int()
i = int()
a = int(input("Ingrese el valor de A: "))
b = int(input("Ingrese el valor de B: "))
resultado = 1
for i in range(1,b+1):
	resultado = resultado*a
print("El resultado de ",a," elevado a ",b," es: ",resultado)

