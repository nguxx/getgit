'''
.Écrivez un programme qui analyse un par un tous les éléments d'une liste de mots (par exemple :   [ ' Jean ' ,  ' Maximilien ' ,  ' Brigitte ' ,  ' Sonia ' ,  ' Jean-Pierre ' ,  ' Sandra ' ]  ) pour générer deux nouvelles listes. L'une contiendra les mots comportant moins de 6 caractères, l'autre les mots comportant 6 caractères ou davantage. Et si un nom fait plus de 10 caractère (Jean-Pierre), l'effacer de la liste
/!\ Tel quel, il va y avoir un probleme car len(l[i]) va compter tout les caractères, même les espaces : donc tous les noms vont faire plus de 6 caractères et l6 sera vide
'''
# l = [ ' Jean ' ,  ' Maximilien ' ,  ' Brigitte ' ,  ' Sonia ' ,  ' Jean-Pierre ' ,  ' Sandra ' ]
l = ['0_Jean' ,  '1_Maximilien' ,  '2_Brigitte' ,  '3_Sonia' , '4_Jean-Pierre', '5_Sandra', '6_Marie-Anaïs', '7_Loïs', '8_Aurélien-Pierre', '9_LeopoldineAlEau']
i = 0
j = 0
l6 = []
lautre = []
#ldepartCor = []
efface =[]
print('liste de départ :')
for nom in l:
	print(nom, 'len(nom) =', len(nom))

while i < len(l):
	#ldepartCor = l[i]
	if len(l[i]) <8:
		l6.append(l[i])
	else:
		lautre.append(l[i])
	i = i + 1
print('--------------------------')
print('l =',l)
while j < len(l):
    print('in boucle : l avant del =', l)
    del(l[j])
    print('in boucle : l après del =', l)
    print('j =', j, '|', 'len(l) =,', len(l))
    j+=1
'''
for nom in l:
	print('nom for =', nom)
	if len(nom) > 12:
		efface.append(nom)
		print('len(nom)>12 =', nom)
		#print('l[',j,']=', l[j])
		del(nom)
'''
# affichage des listes elles-mêmes, avec les crochets
print (end='\n')
print('la liste "l6" des noms de moins de 8 lettres :', '\n', l6)
print ('la liste "lautre" des noms de au moins 8 lettres :','\n',  lautre)
print ('la liste de départ corrigée des noms > 12 lettres :','\n',  l)
print ('liste des noms effacés :', '\n', efface)
'''
# avec un affichage propre des items des listes, sans les crochets
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
	'''
