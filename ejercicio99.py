totalventa = float()
montodescuento = float()
totalpagar = float()
tipocliente = str()
totalventa = float(input("Ingrese el monto total de la venta (en Bs): "))
tipocliente = input("Ingrese el tipo de cliente (A para común, B para especial): ")
if (tipocliente=="A" or tipocliente=="B"):
	if (totalventa>700):
		montodescuento = totalventa*0.01
	else:
		montodescuento = 0
else:
	montodescuento = totalventa*0.02
totalpagar = totalventa-montodescuento
print("Monto de descuento: ",montodescuento," Bs")
print("Total a pagar: ",totalpagar," Bs")

