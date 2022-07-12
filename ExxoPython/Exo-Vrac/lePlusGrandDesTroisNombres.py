# Utilisation d'une liste et de branchements conditionnels
 
print("Ce script recherche le plus grand de trois nombres")
print("Veuillez entrer trois nombres séparés par des virgules : ")
ch =input()
#Note : l'association des fonctions eval() et list() permet de convertir en liste toute chaîne de valeurs séparées par des virgules. En fait, la fonction eval() évalue le contenu de la chaîne fournie en argument comme étant une expression Python dont elle doit renvoyer le résultat. Par exemple :  eval("7 + 5") renvoie l'entier 12. Si on lui fournit une chaîne de valeurs séparées par des virgules, cela correspond pour elle à un tuple. Les tuples sont des séquences apparentées aux listes. Ils seront abordés au chapitre 10 (cf. page 199).
nn = list(eval(ch))
print(nn)
max, index = nn[0], 'premier'
print('max =', max)
print('nn[0] =', nn[0])
print('index =', index)
if nn[1] > max: 	    # ne pas omettre le double point !
    max = nn[1]
    index = 'second'
if nn[2] > max:
    max = nn[2]
    index = 'troisième'
print("Le plus grand de ces nombres est", max)
print("Ce nombre est le", index, "de votre liste.")