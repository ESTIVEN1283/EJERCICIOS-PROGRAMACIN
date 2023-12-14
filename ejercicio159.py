cantidadcuadernos = int()
montototal = float()
print("Ingrese la cantidad de cuadernos a comprar: ")
cantidadcuadernos = int(input())
if (cantidadcuadernos<12):
	montototal = cantidadcuadernos*5
else:
	montototal = cantidadcuadernos*7
print("El monto total a pagar es: ",montototal,"bs")

