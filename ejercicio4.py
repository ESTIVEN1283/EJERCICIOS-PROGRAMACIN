mes = int(input("Ingrese el número del mes: "))
# Proceso para calcular los días en el mes
if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
	print(("El mes tiene 31 días."))
elif mes==4 or mes==6 or mes==9 or mes==11:
	print(("El mes tiene 30 días."))
elif mes==2:
	print(("El mes de febrero puede tener 28 o 29 días, dependiendo de si es un año bisiesto o no."))
elif mes==otrocaso:
	print(("Número de mes no válido. Ingrese un número de mes entre 1 y 12."))

