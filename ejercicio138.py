a = int()
b = int()
temp = int()
mcd = int()
mcm = int()
a = int(input("Ingrese el primer número (a): "))
b = int(input("Ingrese el segundo número (b): "))
temp = 0
mcd = 0
mcm = 0
# Calcular el MCD
if a<b:
	temp = a
	a = b
	b = temp
for temp in range(b,0,-1):
	if a%temp==0 and b%temp==0:
		mcd = temp
# Calcular el MCM
mcm = (a*b)/mcd
print("El MCD de ",a," y ",b," es: ",mcd)
print("El MCM de ",a," y ",b," es: ",mcm)
