chaine ="Monty Python, ee"
cara = "e"
i = 0 #l'indice
t = 0 #le drapeau
print('La chaine de cacatère: "', chaine, '"',end = " ")
while i < len(chaine):
    if chaine[i] == cara :
	    t = t + 1
    i = i + 1
if t == 1:
	print("contient le caractère :", cara, end = " ")
elif t > 1:
	print("contient plusieurs caractères :", cara, end = " ")
else :
	print("ne contient pas le caractère :", cara, end = " ")
print("parmi les", len(chaine), "caractères")
jour = ['lundi', 'mardi', 'mercredi', 1800, 20.357, 'jeudi', 'vendredi']
print("\n")
print("print(jour) donne :","\n",jour)
print("print(jour[0], jour[2], jour[4]) donne :")
print(" ", jour[0], jour[2], jour[4])
jour[2] = "mercredi modifié"
print("\n")
print("Après une nouvelle entrée, print(jour[0], jour[2], jour[4]) donne maintenant :", end = " ")
print(jour[0], jour[2], jour[4])
print("\n")
print("la fonction del() permet de supprimer en fonction de l'index. ex: del(jour[2]")
del(jour[2])
print(jour)
