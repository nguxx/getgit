a, b, c = 1, 1, 1
while c < 11 :
	print(b, end =" ")
	a, b, c = b, a+b, c+1 #la valeur a est avant la valeur b donc elle prend la valeur de b avant que b = a+b