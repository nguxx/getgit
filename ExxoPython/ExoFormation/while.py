#
#while True:
#    print("spam!") #boucle infinie
#--------------------
#a = 0
#while (a < 7):
#    print(a)
#    a = a + 1
#print("a =",a)
#-------Suite de Fibonacci----------
# le nombre qui suit est l'addition des deux nobre précédent-
'''
a, b, c = 1, 1, 1
while c < 11 :
    print(b, end="-") #end=" " permet d'afficher sur une ligne
    a, b, c = b, a+b, c+1 #la valeur a est avant la valeur b donc elle prend la valeur de b avant que b = a+b
print()

'''
a, b, c = 1, 1, 1
while c < 11 :
    print(b,a,sep="__", end=" ") #end=" " permet d'afficher sur une ligne
    b = a+b
    a = b
    c = c+1
print()
##----------inbrication While et if-------
#i = 0
#while True:
#    i = i + 1
#    print(i)
#    if i > 3:
#        break
#
