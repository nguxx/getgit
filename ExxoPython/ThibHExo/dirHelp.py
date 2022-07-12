#! /usr/bin/env python3
##Utilisation du module dir et help pour afficher les fonctiosn des modules

import random
from pprint import pprint  #permet d'afficher à la ligne, lible pour dir()

#pprint(dir(random))
#affiche les fonction à la suite
# les fonction avec underscore sont des fonctions privées

#help(random.randint) # on ne met pas les parenthèses, on ne cherche pas à appeler la fonction
# va chercher les docstrings, si elle sont là.
 
#print(callable(pprint))
# cela va renvoyer True la fonction est appelable. 
# Mais si je n'avais que importé le module pprint (import pprint) sans la fonction ce serait False.
# exemple avec os, puis os.name
# il faut bien sur importer os
import os

print(callable(os.name))
print(os.name)
