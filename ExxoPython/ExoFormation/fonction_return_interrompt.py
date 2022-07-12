def additionner(x, y):
    return x + y

a = 3
b = 4
c = additionner(a, b)   # encore une assignation
print(c)

#-----------------------------------
# return interrompt aussi l'execution de la fonction
def dire_bonjour(prénom, première_fois=False):
    print("Bonjour", prénom)
    if not première_fois:
            return
    print("Heureux de faire votre connaissance")

dire_bonjour("Dimitri", première_fois=True)
#dire_bonjour("Dimitri", première_fois=False)

