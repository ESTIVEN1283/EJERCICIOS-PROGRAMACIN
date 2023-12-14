monto = float()
montoconrecargo = float()
deseafactura = str()
print("Ingrese el monto: ")
monto = float(input())
print("¿Desea factura? (S/N): ")
deseafactura = input()
if deseafactura=="S" or deseafactura=="s":
	# Calcular el monto con recargo del 13%
	montoconrecargo = monto+(monto*0.13)
	print("El monto con recargo del 13% es: ",montoconrecargo)
else:
	# No hay recargo, mostrar el monto original
	print("El monto es: ",monto)
