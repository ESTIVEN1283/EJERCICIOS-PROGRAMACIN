# Declaración de variables
angulo1_grados = int()
angulo1_minutos = int()
angulo2_grados = int()
angulo2_minutos = int()
angulo3_grados = int()
angulo3_minutos = int()
# Entrada de datos
print("Ingrese el primer ángulo en grados: ")
angulo1_grados = int(input())
print("Ingrese los minutos del primer ángulo: ")
angulo1_minutos = int(input())
print("Ingrese el segundo ángulo en grados: ")
angulo2_grados = int(input())
print("Ingrese los minutos del segundo ángulo: ")
angulo2_minutos = int(input())
print("Ingrese el tercer ángulo en grados: ")
angulo3_grados = int(input())
print("Ingrese los minutos del tercer ángulo: ")
angulo3_minutos = int(input())
# Verificar si los ángulos forman un triángulo válido
if (angulo1_grados+angulo2_grados+angulo3_grados==180) and (angulo1_minutos+angulo2_minutos+angulo3_minutos<60):
	print("Los ángulos forman un triángulo válido.")
else:
	print("Los ángulos no forman un triángulo válido.")
