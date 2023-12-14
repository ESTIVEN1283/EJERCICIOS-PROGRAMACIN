salario = float()
bono = float()
ant = int()
print("Ingresar el salario del trabajador: ")
salario = float(input())
print("Ingresar los años de antigüedad del trabajador: ")
ant = int(input())
if (salario<2000 or ant>4):
	bono = (salario*0.25)+salario
else:
	bono = (salario*0.20)+salario
print("El bono navideño del trabajador es: ",bono)
