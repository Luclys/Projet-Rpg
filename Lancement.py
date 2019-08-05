#Ici on met les persos + les items pour test les fonctions et les classes
from Visualisation import *
import time
import platform
import os

Poudre_magique = Item("Poudre de perlinpainpain",50,3, 10, "C'est une poudre magiiiiique !")
Ronce_demoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
Epee_maudite = Equipement("Epee maudite", 1,90,1, 5, 0, 2, 0, 0,"Ceci est l'épée maudite !","","","main")
Casque_WazukiIV = Equipement("Casque du roi Wazuki IV", 1,1,1, 0, 10, 0, 200, 2,"Vieux casque dégueulasse","","","tete")
Potion_soin = Consommable("Potion de soin",1,1,1,"Potion qui soigne 2 pv", 2, 12)
Brulure = Effet("Brûlure", 2 , 2, "Au secours ça brule !")
Poison = Effet("Poison", 2 , 2, "J'ai mal")
Purge = Effet("Purge", 2 , 1, "Je suis guérie !")
Gluant = Monstre("Gluant", 5, 13, 20, 1, [Poudre_magique, Ronce_demoniaque], Brulure, 1)
Multi_Gluant = Monstre("Multi Gluant", 5, 13, 20, 1, [Epee_maudite], Poison, 2)
Boule_de_feu = Sort("Boule de feu", 50, "C'est une boule de feu", 10, 0, Brulure, 1)
Glace = Sort("Glace", 50, "Non ce n'est pas celle que tu manges l'été", 10, 0, Purge, 2)
Mage = Classe("Mage",[Boule_de_feu.nom, Glace.nom])
Guerrier = Classe("Guerrier",[])
Paladin = Classe("Paladin",[])
Ish = PNJ("Ish", [Epee_maudite.nom, Casque_WazukiIV.nom])

Plaine = Zone("Plaine", [Gluant, Multi_Gluant], "C'est une plaine")

#Classe disponible (ici juste le string. Nécessite une fonction pour attribuer les sorts et les items de base)
classeDispo = ['Mage', 'Paladin', 'Guerrier']

def menuPrincipale(perso):
    if os.path.isdir("perso/"):
        loadAll()
    continuer = True
    while continuer:
        print("1.Nouveau personnage \n2.Charger un personnage !\n3.Quitter\n")
        choix = input('Que voulez-vous faire ? : ')
        if choix == '1':
            clean()
            print('\n**********************************************************************************************\n'\
                  + 'Bienvenue dans la création de personnage !\n'\
                  + "Le jeu n'a pas encore d'interface mais vous verrez même en mode console il est très sympa :) ! \n"\
                  + '**********************************************************************************************\n')
            time.sleep(2)
            nom = input('Pour commencer entrez le nom de votre Héro ! : ')
            nom_joueur = list()
            if len(joueur) != 0:
                for j in joueur:
                    nom_joueur.append(j.nom)
            while nom in nom_joueur:
                nom = input('\n***Euh excuse moi mais tu as déjà un perso qui se nomme ' + nom + ' D: ***\n'\
                            +'Entre un autre nom ! : ')
            print('\nSuper ! Maintenant tu dois choisir ta classe \n\nVoici les classes disponibles :')
            time.sleep(1)
            classe = input("\n- " + '\n- '.join(classeDispo) + '\n\nFais ton choix : ')
            while classe not in classeDispo: #Si l'individu choisi une classe qui n'existe pas (petit coquin)
                classe = input("Cette classe n'existe pas \nSelectionne une des classes si dessous : \n- " + '\n- '.join(classeDispo) + '\n Fais ton choix : ')
            #CREATION DU JOUEUR ON LE STOCK DANS LA LISTE 'joueur' car sinon il ne peut pas etre réutilisé    
            perso[0] = creerPerso(nom, randint(1,5), randint(1,5)\
                                     , randint(1,5), randint(1,5), randint(1,5), classe\
                                     , randint(1,5),randint(1,5),randint(1,5),randint(1,5)\
                                     ,randint(1,5),randint(1,5), eval(classe).get_sort(), dict())
            joueur.append(creerPerso(nom, randint(1,5), randint(1,5)\
                                     , randint(1,5), randint(1,5), randint(1,5), classe\
                                     , randint(1,5),randint(1,5),randint(1,5),randint(1,5)\
                                     ,randint(1,5),randint(1,5), eval(classe).get_sort(), dict()))

            print('\nVoila ton aventure peut démarrer jeune héro !\n')
            time.sleep(1.2)
            print('Tu vas rejoindre ce monde extraordinaire peuplé par des créatures hors du commun !\n\n')
            savePerso(perso[0])
            time.sleep(1.2)
            hub(perso[0])
        elif choix == '2':
            clean()
            nom_joueur = list()
            print('\n**********************************************************************************************\n'\
                  + '******************************Sélectionne un de tes personnages*******************************')
            for i in joueur:
                print('***' + i.nom + ' - Niveau : ' + str(i.niveau))
                nom_joueur.append(i.nom)
            print('**********************************************************************************************\n')
            if nom_joueur :
                choix_perso = input('\n\nFais ton choix : ')
                while choix_perso not in nom_joueur: 
                    choix_perso = input("Ce personnage n'existe pas \nSelectionne un des personnages existants ! :\n")
                index = nom_joueur.index(choix_perso)
                perso[0] = joueur[index]
                print('\nPersonnage chargé ! Bon jeu ! :)\n\n')
                time.sleep(1.2)
                clean()
                hub(perso[0])
            else:
                print('Aucun personnage dans votre sauvegarde :/\n\n')
        elif choix == '3':
            print('Bye ! Reviens vite !')
            time.sleep(1)
            continuer = False
        else :
            print('\n***Commande inconnue :(***\n\n')


            
def hub(perso):
    continuer = True
    while continuer:
        print('\n**********************************************************************************************\n'\
            + 'Hey ' + perso.nom + ' !\n'\
            + "1.Virée en donjon \n2.Sauvegarder !\n3.Retour au menu principal\n"\
            + '**********************************************************************************************\n')
        choix = input('Que voulez-vous faire ? : ')
        if choix == '2':
            savePerso(perso)
            
        elif choix == '3':
            clean()
            continuer = False

        else:
            print('\n***Commande inconnue :(***\n\n')



    
def clean():   
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
            
if __name__ == '__main__':
    menuPrincipale(perso)
