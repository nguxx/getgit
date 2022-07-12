'''
Écrivez un programme qui analyse un par un tous les éléments d'une liste de nombres [32, 5, 12, 8, 3, 75, 2, 15] pour générer deux nouvelles listes. L'une contiendra seulement les nombres pairs de la liste initiale, et l'autre les nombres impairs. Par exemple, si la liste initiale est celle de l'exercice précédent, le programme devra construire une liste pairs qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce : pensez à utiliser l'opérateur modulo (%) déjà cité précédemment.
'''
l =  [32, 5, 12, 8, 3, 75, 2, 15]
i = 0
lpairs = []			# crée une liste vide
limpairs = []		# crée une liste vide
while i < len(l):
	a = l[i]%2
	#print('a = ', a) 
	#print('i = ', i)
	if a == 0:
		lpairs.append(l[i])
	else:
		limpairs.append(l[i])
	i = i+1
print('la liste "lpairs" :', lpairs)
print('la liste "limpairs" :', limpairs)
