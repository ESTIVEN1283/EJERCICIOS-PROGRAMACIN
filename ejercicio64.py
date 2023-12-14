n = int()
i = int()
while True:# no hay 'repetir' en python
	n = int(input("ingrese la cantidad de numeros a imprimir: "))
	if n>=2: break
for i in range(1,n+1):
	if i%2==0:
		print(" ",i, end="")#end para mostrar sin saltar
print("")

