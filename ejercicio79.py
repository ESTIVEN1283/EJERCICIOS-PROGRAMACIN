lado1 = float()
lado2 = float()
lado3 = float()
lado1 = float(input("Ingrese la longitud del primer lado: "))
lado2 = float(input("Ingrese la longitud del segundo lado: "))
lado3 = float(input("Ingrese la longitud del tercer lado: "))
# Verificación de la condición para formar un triángulo
if ((lado1+lado2>lado3) and (lado1+lado3>lado2) and (lado2+lado3>lado1)):
	print("Las longitudes ingresadas pueden formar un triángulo.")
else:
	print("Las longitudes ingresadas NO pueden formar un triángulo.")

