i = int()
num = int()
may = int()
minu = int()
suma = int()
pro = int()
n = int(input("ingrese la cantidad de numeros: "))
num = [int() for ind0 in range(n)]
for i in range(n):
	print("ingrese los numeros a comparar: ",i+1,": ")
	num[i] = int(input())
for i in range(n):
	may = num[0]
	minu = num[0]
	for i in range(1,n):
		# aqui encontramos al elemnto mayor
		if num[i]>may:
			# aqui encontramos al elemnto mayor
			may = num[i]
		if num[i]<minu:
			minu = num[i]
suma = 0
for i in range(n):
	suma = suma+num[i]
	pro = int(suma/n)
print("num = | ", end="")
for i in range(n):
	print(num[i]," | ", end="")
print("")
print("El elemnto mayor es = ",may)
print("El elemnto menor es = ",minu)
print("suma = ", suma)
print("promedio = ",pro)
