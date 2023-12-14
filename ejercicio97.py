dado1 = int()
dado2 = int()

while True:# no hay 'repetir' en python
	dado1 = int(input("Ingrese el valor del primer dado: "))
	dado2 = int(input("Ingrese el valor del segundo dado: "))
	if dado1<=6 and dado2<=6: break
# Verificar si son iguales y pares
if dado1==dado2 and dado1%2==0:
	print("¡Ganaste!")
else:
	print("Perdiste")
