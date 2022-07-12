#! /usr/bin/python3.8
# Crér des repertoires avec le module os

import os

chemin = "."
dossier = os.path.join(chemin, "DosTestModule_os")
# pour creer une dossier et un sous dossier
#dos_sous_dos = os.path.join(chemin, "Dos", "SousDos", "ssDos")
#print(dos_sous_dos)
# Pour savoir si le dossier existe (sinon ça plante)
#os.makedirs(dossier, exists_ok=True)
# oubien
if not os.path.exists(dossier):
    os.makedirs(dossier)

# pour effacer le dossier
# if os.path.exists(dossier):
#     os.removedirs(dossier)
