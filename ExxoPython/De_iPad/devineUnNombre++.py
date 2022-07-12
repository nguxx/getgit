
# deviner un nombre choisi au hasard par l'ordi
# + affiche le nombre d'essais
# ++ demander le nom d'utilisateur en début de chaque partie, enregistre le nombre d'essais et féliciter le joueur s'il bat un record.
#import random
#nombre = random.randint(0, 100)
nombre = 50
print('Bonjour, comment t\'appelles tu? entre ton nom STP :')
nom_joueur = input()
print('Enchanté '+ nom_joueur + ', ' + 'on joue?' + '\n' + 'Allez,devine le nombre auquel je pense :')
score = 0
highscore = 0
nbre_parties = 0
i = 0
a = 0
while True:
	if score >= highscore :
		while True:
            #print('nombre_devine')
			nombre_devine = int(input())
			i = i+1
			#score = score + 1
			print("Nombre d'essai :", i)
			if nombre_devine > nombre:
				print("trop grand")
			elif nombre_devine < nombre:
				print("trop petit")
			else:
				print('Barvo '+ nom_joueur + '! Tu as trouvé!' )
				score = i
				#print('bravo '+ nom_joueur + 'ton score est de :', score)
                if highscore  = a :
                    highscore = score
                elif highscore < score:
                    break
                else:   
                    print ('Pour l\'instant ton meilleur score est de :', highscore)
                    print('Si tu veux rejouer pour ameliorer et diminuer ton meilleur score, tape "oui" ou "non" (sans les guillemets ;-)')
                    print('variable rejoue')
                    rejoue = input()
                    if rejoue == 'non':
                        print ('Tanpis ' + nom_joueur + 'à une autre fois alors... :\')')
                        break
                    elif rejoue == 'oui':
                        print("c'est reparti! Entre un nombre :")
                        i = 0
                        #highscore = score
                    else:
                        print("Tu as fais une erreur, j'ai bogué...¯\_(ツ)_/¯... Adieu!" )
                        break
	elif score < highscore:
		print("Tu viens d'ameliorer ton meilleure score, Bravo!")
		print('Tu veux faire une autre partie ? (tape "oui" ou "non")')
		#print('new_partie')
		new_partie = input()
		if new_partie == 'non':
			print ('Tanpis ' + nom_joueur + 'à une autre fois alors... :\'\)')
			break
		elif new_partie == 'oui' :
			 nbre_parties = nbre_parties + 1
			 print("CoooOOoool! c'est reparti!")
		else: 
			print("Tu as fais une erreur, j'ai bogué...¯\_(ツ)_/¯... Adieu!" )
			break
		
		
				
			
