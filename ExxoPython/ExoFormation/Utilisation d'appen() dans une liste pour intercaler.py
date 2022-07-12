"""
Écrivez un petit programme qui crée une nouvelle liste t3. Celle-ci devra contenir tous les éléments des deux listes en les alternant, de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant :

[ ' Janvier ' ,31, ' Février ' ,28, ' Mars ' ,31, etc...].
"""

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
t2 = [ ' Janvier ' ,  ' Février ' ,  ' Mars ' ,  ' Avril ' ,  ' Mai ' ,  ' Juin ' , ' Juillet ' ,  ' Août ' ,  ' Septembre ' , 'Octobre ' ,  ' Novembre ' ,  ' Décembre ' ]
t3 = []
a = 0
while a < len(t1):
	t3.append(t2[a])
	t3.append(t1[a])
	#print(t3)
	a = a + 1
print(t3)

