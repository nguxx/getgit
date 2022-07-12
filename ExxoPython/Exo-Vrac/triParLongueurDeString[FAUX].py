'''
.Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots (par exemple :   [ ' Jean ' ,  ' Maximilien ' ,  ' Brigitte ' ,  ' Sonia ' ,  ' Jean-Pierre ' ,  ' Sandra ' ]  ) pour générer deux nouvelles listes. L'une contiendra les mots comportant moins de 6 caractères, l'autre les mots comportant 6 caractères ou davantage. Et si un nom fait plus de 10 caractère (Jean-Pierre), l'effacer de la liste
/!\ Tel quel, il va y avoir un probleme car len(l[i]) va compter tout les caractères, même les espaces : donc tous les noms vont faire plus de 6 caractères et l6 sera vide
'''
# l = [ ' Jean ' ,  ' Maximilien ' ,  ' Brigitte ' ,  ' Sonia ' ,  ' Jean-Pierre ' ,  ' Sandra ' ]
l = ['Jean' ,  'Maximilien' ,  'Brigitte' ,  'Sonia' ,  'Jean-Pierre' ,  'Sandra']
i = 0
l6 = []
lautre = []
ldepart = []
print('liste de départ =', end=' ')
while i < len(l):
	ldepart = l[i]
	print(ldepart, end=', ')
	#print('ln(l[i]) =', len(l[i]))
	if len(l[i]) > 10:
		del(l[i])
	elif len(l[i]) < 6:
		l6.append(l[i])
	else:
		lautre.append(l[i])
	i = i + 1
'''
print (end='\n')
print('la liste "l6" des noms de moins de 6 lettres :', l6)
print ('la liste "lautre" des noms de au moins 6 lettres :', lautre)
print ('la liste de départ corrigée des noms > 10 lettres :', l)
'''
# avec un affichage propre
print (end='\n')
print('la liste "l6" des noms de moins de 6 lettres :', end =' ')
il6 = 0 
while il6 < len(l6):  
	print( l6[il6], end =', ')
	il6 = il6 + 1
ilautre = 0
print (end='\n')
print('la liste "lautre" des noms de au moins de 6 lettres :', end =' ')
while ilautre < len(lautre):  
	print(lautre[ilautre], end =', ')        
	ilautre = ilautre + 1
il = 0
print(end='\n')
print('la liste de départ corrigée des noms > 10 lettres :',end =' ')          
while il < len(l):  
	print(l[il], end =', ')          
	il = il + 1
