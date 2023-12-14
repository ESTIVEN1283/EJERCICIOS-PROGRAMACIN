import random
v = int()
i = int()
j = int()
p = int()
ip = int()
ii = int()
dim = int(input("ingrese la dimension del vector: "))
v = [int() for ind0 in range(dim)]
p = [int() for ind0 in range(dim)]
j = [int() for ind0 in range(dim)]
for i in range(dim):
	v[i] = random.randint(5, 36)
ip = 0
ii = 0
for i in range(dim):
	if v[i]%2==0:
		p[ip] = v[i]
		ip = ip+1
	else:
		j[ii] = v[i]
		ii = ii+1
print("")
print("v = | ", end="")
for i in range(dim):
	print(v[i]," | ", end="")
print("")
print("v = | ", end="")
for i in range(ip):
	print(p[i]," | ", end="")
print("")
print("v = | ", end="")
for i in range(ii):
	print(j[i]," | ", end="")
print("")
