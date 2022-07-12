# une utilisation intelligente du modulo
jour = ['lundi','mardi','mercredi','jeudi','vendredi','samedi', 'dimanche'] 
a, b = 0, 0 
while a<25:
    a = a + 1  
    b = a % 7
    if b!=0:
    	print(a,  "b + 1 donne le", b+1, 'ème jour de la semaine  :', jour[b] )
    else:
    	print(a,  "b + 1 donne le", b+1, 'er jour de la semaine  :', jour[b] )
