num = int()
a = int()
b = int()
c = int()
num = int(input("Ingrese un número: "))
a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
if num%a==0:
	print(num," es múltiplo de ",a)
if num%b==0:
	print(num," es múltiplo de ",b)
if num%c==0:
	print(num," es múltiplo de ",c)
if num%a!=0 and num%b!=0 and num%c!=0:
	print(num," no es múltiplo de ",a,", ",b," ni ",c)

