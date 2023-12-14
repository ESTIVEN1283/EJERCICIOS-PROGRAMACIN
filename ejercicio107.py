dianacimiento = int()
mesnacimiento = int()
anionacimiento = int()
diaactual = int()
mesactual = int()
anioactual = int()
edadanios = int()
edadmeses = int()
edaddias = int()
dianacimiento = int(input("Ingrese la fecha de nacimiento: "))
mesnacimiento = int(input("Ingrese el mes de nacimiento: "))
anionacimiento = int(input("Ingrese el año de nacimiento: "))
# Entrada de la fecha actual
diaactual = int(input("Ingrese la fecha actual: "))
mesactual = int(input("Ingrese el mes actual de nacimiento: "))
anioactual = int(input("Ingrese el año actual de nacimiento: "))
# Calcular la edad en años, meses y días
edadanios = anioactual-anionacimiento
edadmeses = mesactual-mesnacimiento
edaddias = diaactual-dianacimiento
# Ajustar la edad si los meses o días son negativos
if edadmeses<0:
	edadanios = edadanios-1
	edadmeses = 12+edadmeses
if edaddias<0:
	# Restar los días del mes anterior
	edadmeses = edadmeses-1
	if mesactual-1==0:
		edaddias = 31+edaddias
	else:
		# Consideramos un año no bisiesto para simplificar
		edaddias = 30+edaddias
# Mostrar la edad calculada
print("La edad es: ",edadanios," años, ",edadmeses," meses y ",edaddias," días.")

