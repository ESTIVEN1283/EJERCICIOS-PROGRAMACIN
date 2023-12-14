suma = int()
men = int()
may = int()
medio = int()
prom = int()
n1 = int(input("ingrese su primera nota: "))
n2 = int(input("ingrese su segunda nota: "))
n3 = int(input("ingrese su tercera nota: "))
suma = (n1+n2+n3)
men = n3
may = n2
if n1<men:
	men = n1
if n2<men:
	men = n2
if n1>may:
	may = n1
if n3>may:
	may = n3
medio = (suma-may-men)
prom = int((may+medio)/2)
print("el promedio de las dos notas mayores es: ",prom)
