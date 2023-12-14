nota1 = float()
nota2 = float()
nota3 = float()
promedio = float()
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
promedio = (nota1+nota2+nota3)/3
if (promedio>51):
	print("Promedio:",promedio)
	print("Aprobado")
else:
	print("Promedio:",promedio)
	print("Reprobado")

