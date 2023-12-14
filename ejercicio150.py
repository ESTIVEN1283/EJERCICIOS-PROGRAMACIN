grados1 = int()
minutos1 = int()
grados2 = int()
minutos2 = int()
sumagrados = int()
sumaminutos = int()
print("Ingrese el primer ángulo:")
print("Grados:")
grados1 = int(input())
print("Minutos:")
minutos1 = int(input())
print("Ingrese el segundo ángulo:")
print("Grados:")
grados2 = int(input())
print("Minutos:")
minutos2 = int(input())
sumagrados = grados1+grados2
sumaminutos = minutos1+minutos2
if sumaminutos>=60:
	sumaminutos = sumaminutos-60
	sumagrados = sumagrados+1
if sumagrados==180 and sumaminutos==0:
	print("La suma de los ángulos es 180 grados.")
else:
	print("La suma de los ángulos no es 180 grados.")

