# deviner un nombre choisi au hasard par l'ordi
# et affiche le nombre d'essais
import random
nombre = random.randint(0, 100)
print("devine le nombre auquel je pense")
i = 0
while True:
	nombre_devine = int(input())
	i = i+1
	print("le nombre d'essai :", i)
	if nombre_devine > nombre:
		print("trop grand")
	elif nombre_devine < nombre:
		print("trop petit")
	else:
		print("bravo")
		break
		print()
