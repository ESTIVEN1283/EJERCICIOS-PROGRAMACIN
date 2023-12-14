x = float()
ye = float()
x = float(input("Ingrese la coordenada x:"))
ye = float(input("Ingrese la coordenada y:"))
if x>0 and ye>0:
	print("El punto (",x,",",ye,") se encuentra en el primer cuadrante.")
else:
	if x<0 and ye>0:
		print("El punto (",x,",",ye,") se encuentra en el segundo cuadrante.")
	else:
		if x<0 and ye<0:
			print("El punto (",x,",",ye,") se encuentra en el tercer cuadrante.")
		else:
			if x>0 and ye<0:
				print("El punto (",x,",",ye,") se encuentra en el cuarto cuadrante.")
			else:
				print("El punto (",x,",",ye,") se encuentra en el origen.")
