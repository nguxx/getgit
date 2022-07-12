#.Écrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13, 
# mais n'affiche que ceux qui sont des multiples de 7.
a, a2 = 1, 0
while a <= 50:
	b, a = a * 7, a + 1 
	if b % 3 == 0:
		a2 = a2 + 1
		print (b, end=" ") # vérif : la somme des chiffres du résultat est divisible par 3
print("\n","il y a", a2,"nombres divisibles par 3 parmi les 50 premiers résultats de la table de 7")