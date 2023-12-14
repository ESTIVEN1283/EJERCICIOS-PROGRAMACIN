sumadivisores1 = int()
sumadivisores2 = int()
i = int()
j = int()
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
# Calcular la suma de los divisores propios de num1
sumadivisores1 = 0
for i in range(1,int(num1/2)+1):
	if num1%i==0:
		sumadivisores1 = sumadivisores1+i
# Calcular la suma de los divisores propios de num2
sumadivisores2 = 0
for j in range(1,int(num2/2)+1):
	if num2%j==0:
		sumadivisores2 = sumadivisores2+j
# Verificar si son números amigos
if sumadivisores1==num2 and sumadivisores2==num1:
	print(num1," y ",num2," son números amigos.")
else:
	print(num1," y ",num2," no son números amigos.")

