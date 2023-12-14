h = int()
m = int()
s = int()
hora = int(input("ingrese la hora: "))
minu = int(input("ingrese los minutos: "))
seg = int(input("ingrese los segundos: "))
h = 24
m = 60
s = 3600
if hora>h:
	hora = hora-h
else:
	hora = h-hora
if minu>m:
	minu = minu-m
else:
	minu = m-minu
if seg<3600:
	seg = 3600-seg
print("faltan ",hora,".hrs : ",minu,".min : ",seg,".seg para culminar el dia")
