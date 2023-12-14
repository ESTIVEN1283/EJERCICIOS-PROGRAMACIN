import random
dado1 = int()
dado2 = int()
dado3 = int()
sumadados = int()
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
dado3 = random.randint(1,6)
print("Resultado del primer dado: ",dado1)
print("Resultado del segundo dado: ",dado2)
print("Resultado del tercer dado: ",dado3)
sumadados = dado1+dado2+dado3
print("La suma de los resultados es: ",sumadados)
if sumadados>12:
	print("¡Felicidades! Has ganado.")
else:
	print("Lo siento, has perdido.")

