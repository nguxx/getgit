# conversions euros dollars avec suite géométrique des euros
d = 1.65 #taux de l'euro / dollar 1€ = 1.65$
r = 1
e = 1
while e <= 16384 :
    r = 1.65 * e
    print (e, "euro(s) =", r, "dollar(s)")
    e = e * 2
#print(locals())
r = 1.65 #taux de l'euro / dollar 1€ = 1.65$
e = 1
while e <= 16384 :
    print (e, "euro(s) =", r, "dollar(s)")
    r = r * 2
    e = e * 2
