i = int()
n = int()
ant = int()
act = int()
sig = int()
print("ingrese la cantidad de N terminos: ")
n = int(input())
ant = 1
act = 0
for i in range(1,n+1):
	sig = ant+act
	print(sig," ", end="")
	ant = act
	act = sig
print(" ")

