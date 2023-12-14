num = int()
unidad = int()
decena = int()
centena = int()
resultado = str()
unidadtxt = str()
decenatxt = str()
centenatxt = str()
print("Ingrese un número entre 1 y 1000: ")
num = int(input())
# Validar que el número esté en el rango permitido
if num<1 or num>1000:
	print("El número ingresado no está en el rango permitido.")
else:
	# Descomponer el número en unidades, decenas y centenas
    unidad = num%10
    decena = int(num/10)%10
    centena = int(num/100)%10
    # Convertir las unidades a texto
    if unidad==1:
    	unidadtxt = "uno"
    elif unidad==2:
    	unidadtxt = "dos"
    elif unidad==3:
    	unidadtxt = "tres"
    elif unidad==4:
    	unidadtxt = "cuatro"
    elif unidad==5:
    	unidadtxt = "cinco"
    elif unidad==6:
    	unidadtxt = "seis"
    elif unidad==7:
    	unidadtxt = "siete"
    elif unidad==8:
    	unidadtxt = "ocho"
    elif unidad==9:
    	unidadtxt = "nueve"
    else:
    	unidadtxt = ""
    # Convertir las decenas a texto
    if decena==1:
    	if unidad==0:
    		decenatxt = "diez"
    	elif unidad==1:
    		decenatxt = "once"
    	elif unidad==2:
    		decenatxt = "doce"
    	elif unidad==3:
    		decenatxt = "trece"
    	elif unidad==4:
    		decenatxt = "catorce"
    	elif unidad==5:
    		decenatxt = "quince"
    	else:
            decenatxt = "dieci"+unidadtxt
            elif decena==2:
                decenatxt = "veinte"
            elif decena==3:
                decenatxt = "treinta"
            elif decena==4:
                decenatxt = "cuarenta"
            elif decena==5:
                decenatxt = "cincuenta"
            elif decena==6:
                decenatxt = "sesenta"
            elif decena==7:
                decenatxt = "setenta"
            elif decena==8:
                decenatxt = "ochenta"
            elif decena==9:
                decenatxt = "noventa"
            else:
                decenatxt = ""
    # Convertir las centenas a texto
    if centena==1:
    	centenatxt = "ciento"
    elif centena==2:
    	centenatxt = "doscientos"
    elif centena==3:
    	centenatxt = "trescientos"
    elif centena==4:
       	centenatxt = "cuatrocientos"
    elif centena==5:
    	centenatxt = "quinientos"
    elif centena==6:
    	centenatxt = "seiscientos"
    elif centena==7:
    	centenatxt = "setecientos"
    elif centena==8:
    	centenatxt = "ochocientos"
    elif centena==9:
    	centenatxt = "novecientos"
    else:
    	centenatxt = ""
    # Componer el resultado
    resultado = centenatxt+" "+decenatxt+" "+unidadtxt
    resultado = (resultado)
    print("El número ",num," en palabras es: ",resultado)
