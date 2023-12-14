producto = int()
may = int()
men = int()
i = int()
divisibles = int()
resta = int()
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
# Calcular el producto mediante sumas sucesivas
producto = 0
for i in range(1,num2+1):
	producto = producto+num1
print("El producto de ",num1," y ",num2," es: ",producto)
# Determinar el mayor y el menor
if num1>num2:
	may = num1
	men = num2
else:
	may = num2
	men = num1
# Calcular la división del mayor entre el menor mediante restas sucesivas
divisibles = may
resta = 0
while divisibles>=men:
	divisibles = divisibles-men
	resta = resta+1
print("La división de ",may," entre ",men," es: ",resta)

