import os
chemin = "/home/ngugx/Desktop"
dossier = os.path.join(chemin, "monDossier")
if not os.path.exists(dossier):
    os.makedirs(dossier)
else:
    print("ce nom est déjà pris")
