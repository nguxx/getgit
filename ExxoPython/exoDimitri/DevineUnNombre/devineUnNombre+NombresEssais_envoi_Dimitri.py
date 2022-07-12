# deviner un nombre choisi au hasard par l'ordi
# + affiche le nombre d'essais
# ++ demander le nom d'utilisateur en début de chaque partie, enregistre le nombre d'essais et féliciter le joueur s'il bat un record.
import random
nombre = random.randint(0, 100)
#nombre = 2
print('Bonjour, comment t\'appelles tu? entre ton nom STP :')
nom_joueur = input()
print('Enchanté '+ nom_joueur + ', ' + 'on joue?' + '\n' + 'Allez,devine le nombre auquel je pense entre 1 et 100 :')
score = 1
highscore = 0
highscore_abs = 1
nbre_parties = 1
i = 0
while True:
    if score > highscore :
        while True:
            #print('nombre_devine')
            nombre_devine = int(input())
            i = i+1
            print("Nombre d'essai :", i)
            if nombre_devine > nombre:
                print("trop grand")
            elif nombre_devine < nombre:
                print("trop petit")
            else:
                print('Bravo '+ nom_joueur + '! Tu as trouvé!' )
                score = i
                i = 0
                #print('highscore doit valoir 0 :',highscore)
                if highscore == 0 :     #si c'est le premier tour
                    highscore = score
                    #print('highscore 33 :',highscore)
                    if highscore_abs == 1:      # si c'est le premier tour de la 1ere partie
                        highscore_abs = highscore
                    if highscore_abs > highscore:    # si au premier tour de la Nème partie le premier tour le HS est plus petit que HS_abs on arrete pour feliciter et augmenter le HS_abs
                        #print('44  break')
                        break
                    if highscore == 1:
                        #print ('break 45')
                        break
                elif score <= highscore:         # si le score de la partie est meilleure que le HS de la partie alors on arrete la partie
                    #print('39 break')
                    break
                elif highscore < highscore_abs:
                    #print('if highscore < highscore_abs: break')
                    break
                print ('Pour l\'instant ton meilleur score de cette partie est de :', highscore)
                print('Meilleure score toutes parties confondues: ', highscore_abs,'sur', nbre_parties,'parties')
                print('Si tu veux rejouer pour ameliorer et diminuer ton meilleur score,'+'\n'+'tape "oui" ou "non" (sans les guillemets ;-)')
                #print('variable rejoue entre (oui ou non)')
                rejoue = input()
                if rejoue == 'non':
                    print ('Tanpis ' + nom_joueur + ' à une autre fois alors... :\'-)')
                    print('Tu finis avec un highscore de : ' , highscore_abs)
                    exit()
                elif rejoue == 'oui':
                    print("c'est reparti! Entre un nombre :")
                    score = 0
                else:
                    print("Tu as pas tapé 'oui' ou 'non', j'ai bogué...¯\_(ツ)_/¯..." )
                    print('Dans le doute, je relance la partie... Entre un nombre :')
                    break
    elif score <= highscore:
        #print('66, score =', score, 'highscore=',highscore, 'highscore_abs',highscore_abs)
        highscore = score
        if highscore_abs > highscore:
            highscore_abs = highscore
        if highscore_abs == 1:
            print("\n"+"On peut pas faire mieux! Tu es un champion!"+"\n"+"_________C'est fini " + nom_joueur +"!________"+"\n"+"Tu peux éteindre et aller faire un tour. ;-)" )
            print('Tu finis avec un highscore de : ' , highscore_abs)
            exit()            
        print("Tu viens d'ameliorer ton score, il est maintenant de : " + str(highscore))
        print('Le meilleure score de toutes les parties confondues: ', highscore_abs, 'sur', nbre_parties,'parties')
        print('Veux-tu l\'améliorer Terrien', nom_joueur, '? (tape "oui" ou "non")')
        #print('new_partie')
        new_partie = input()
        if new_partie == 'non':
            print ('Tanpis ' + nom_joueur + ' à une autre fois alors... :\'-\)')
            print('Tu finis avec un highscore de : ' , highscore_abs)
            exit()
        elif new_partie == 'oui' :
             nbre_parties = nbre_parties + 1
             print("CoooOOoool! c'est reparti! Entre un nouveau nombre : ")
             score = 1
             highscore = 0
             #break
        else: 
            print("Tu as pas tapé 'oui' ou 'non', j'ai bogué...¯\_(ツ)_/¯..." )
            print('(89)Dans le doute, je relance un partie... Entre un nombre :')
            #break
