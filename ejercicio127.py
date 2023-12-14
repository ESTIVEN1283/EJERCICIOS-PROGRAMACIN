duracion = float()
costo = float()
duracion = float(input("Ingrese la duración de la llamada en minutos: "))
if duracion<=5:
	costo = 1.5
else:
	if duracion<=10:
		costo = 0.9
	else:
		costo = 0.5
print("El costo de la llamada es: ",costo)

