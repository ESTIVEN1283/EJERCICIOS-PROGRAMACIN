lado1 = float()
lado2 = float()
lado3 = float()
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))
if lado1==lado2 and lado2==lado3:
	print("El triángulo es equilátero.")
if (lado1==lado2 and lado2!=lado3) or (lado1==lado3 and lado3!=lado2) or (lado2==lado3 and lado3!=lado1):
	print("El triángulo es isósceles.")
if lado1!=lado2 and lado1!=lado3 and lado2!=lado3:
	print("El triángulo es escaleno.")

