anio = int(input("ingre el anio que desea saber si es bisiesto o no: "))
if anio%4==0:
	if anio%100==0:
		if anio%400==0:
			print("el anio ",anio," es bisiesto")
		else:
			print("el anio ",anio," no es bisiesto")
	else:
		print("el anio ",anio," es bisiesto")
else:
	print("el anio ",anio," no es bisiesto")
