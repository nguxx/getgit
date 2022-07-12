a, b, c = 1, 1, 1
while c < 50 :
	print(c, ":", b, type(b))
	a, b, c = b, a+b, c+1 #la valeur a est avant la valeur b donc elle prend la valeur de b avant que b = a+b