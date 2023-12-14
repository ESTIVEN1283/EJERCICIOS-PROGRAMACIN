nota = float()
sumanotas = float()
promedio = float()
contador = int()
sumanotas = 0
for contador in range(1,8):
	print("Ingrese la nota ",contador,": ")
	nota = float(input())
	sumanotas = sumanotas+nota
promedio = int(sumanotas/7)
print("El promedio de las 7 notas es: ",promedio)

