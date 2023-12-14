m1 = float()
m2 = float()

print(("Ingrese las coordenadas del primer punto (x1, y1):"))
x1 = float(input())
y1 = float(input())
print(("Ingrese las coordenadas del segundo punto (x2, y2):"))
x2 = float(input())
y2 = float(input())
print(("Ingrese las coordenadas del tercer punto (x3, y3):"))
x3 = float(input())
y3 = float(input())
# Calcular la pendiente de la primera recta (puntos 1 y 2)
if (x2-x1==0):
	print(("La primera recta es vertical, no se puede calcular su pendiente."))
else:
	m1 = (y2-y1)/(x2-x1)
# Calcular la pendiente de la segunda recta (puntos 1 y 3)
if (x3-x1==0):
	print(("La segunda recta es vertical, no se puede calcular su pendiente."))
else:
	m2 = (y3-y1)/(x3-x1)
# Comparar las pendientes para determinar si son paralelas o se intersectan
if (m1==m2):
	print(("Las rectas son paralelas."))
else:
	print(("Las rectas se intersectan."))
