# une utilisation intelligente du modulo
jour = ['lundi','mardi','mercredi','jeudi','vendredi','samedi', 'dimanche'] 
a, b = 0, 0 
while a<7: 
    b = a % 7 #
    if b==0:
        print(a,"le", b+1, 'er jour de la semaine  :', jour[b] ) #b+1 donne lejour de la semaine
    else:
        print(a,  "b + 1 donne le", b+1, 'ème jour de la semaine  :', jour[b] )
    a = a + 1
