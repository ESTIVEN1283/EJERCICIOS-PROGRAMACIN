# Declaración de variables
horastrabajadas = float()
precioporhora = float()
salariototal = float()
horasnormales = float()
horasextra = float()
# Entrada de datos
print("Ingrese las horas trabajadas: ")
horastrabajadas = float(input())
print("Ingrese el precio por hora: ")
precioporhora = float(input())
# Calcular el salario
if horastrabajadas<=35:
	# No hay horas extra
	salariototal = horastrabajadas*precioporhora
else:
	# Calcular horas normales y extra
	horasnormales = 35
	horasextra = horastrabajadas-horasnormales
	# Calcular salario con horas normales y extra
	salariototal = (horasnormales*precioporhora)+(horasextra*(precioporhora*2))
# Mostrar el salario total
print("El salario total es: ",salariototal)

