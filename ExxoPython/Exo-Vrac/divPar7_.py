#.Écrivez un programme qui affiche les 20 premiers termes
# de la table de multiplication par 7, 
# en signalant au passage (à l'aide d'une
# astérisque) ceux qui sont des multiples de 3.
# Exemple : 7 14 21 * 28 35 42 * 49 …
a, b, c = 1, 1, "*"
while a <=20:
	b = a * 7
	a = a + 1
	if b % 3 == 0:
		print(b,c, end=" ")
	else:
		print(b, end=" ")