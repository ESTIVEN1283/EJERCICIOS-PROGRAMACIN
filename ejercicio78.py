base = int()
exponente = int()
resultado = int()
i = int()
base = int(input("Ingrese la base (a): "))
exponente = int(input("Ingrese el exponente (b): "))
resultado = 1
for i in range(1,exponente+1):
	resultado = resultado*base
print("El resultado de ",base," elevado a la ",exponente," es: ",resultado)

