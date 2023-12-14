num1 = float()
num2 = float()
num3 = float()
may = float()
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))
may = (num1+num2+abs(num1-num2))/2
may = (may+num3+abs(may-num3))/2
print("El número mayor es: ",may)

