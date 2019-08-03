#Ici on met les persos + les items pour test les fonctions et les classes
import os.path
from random import *
import pickle
from SauvegardeEtLoad import *
from Classes import *
from FonctionImportante import *
from Visualisation import *
import json
import time
Poudre_magique = Item("Poudre de perlinpainpain",50,20, 10, "C'est une poudre magiiiiique !")
Ronce_demoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
Epee_maudite = Arme("Epee maudite", 1,90,1,"Ceci est l'épée maudite !", 5, 0, 2, 0, 0 ,"","","main")
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
Arthur = Personnage("Arthur",8,10,0,0,0,"Mage",0,0,0,0,0,0,[Boule_de_feu.nom, Glace.nom], dict())
Jean = Personnage("Jean",3,10,0,0,0,"Paladin",0,0,0,0,0,0,[], dict())
Michel = Personnage("Michel",3,10,0,0,0,"Guerrier",0,0,0,0,0,0,[], dict())
Ish = PNJ("Ish", [Epee_maudite.nom, Casque_WazukiIV.nom])

Plaine = Zone("Plaine", [Gluant, Multi_Gluant], "C'est une plaine")

#Classe disponible (ici juste le string. Nécessite une fonction pour attribuer les sorts et les items de base)
classeDispo = ['Mage', 'Paladin', 'Pretre', 'Guerrier']


def menuPrincipale():
    continuer = True
    while continuer:
        print("1.Nouveau personnage \n2.Retour à l'aventure !\n3.Sauvegarder\n4.Quitter")
        choix = input('Que voulez-vous faire ? : ')
        if choix == '1':
            nom = input('Entre ton nom : ')
            classe = input('Entre ta classe : ')
            while classe not in classeDispo: #Si l'individu choisi une classe qui n'existe pas (petit coquin)
                classe = input("Cette classe n'existe pas \nSelectionne une des classes si dessous : \n- " + '\n- '.join(classeDispo) + '\n Fais ton choix : ')
            #CREATION DU JOUEUR ON LE STOCK DANS LA LISTE 'joueur' car sinon il ne peut pas etre réutilisé    
            joueur.append(creerPerso(nom, randint(1,5), randint(1,5)\
                                     , randint(1,5), randint(1,5), randint(1,5), classe\
                                     , randint(1,5),randint(1,5),randint(1,5),randint(1,5)\
                                     ,randint(1,5),randint(1,5), speelFromClasse(classe), dict()))
            showPerso(joueur[0])
        elif choix == '2':
            loadAll()
        elif choix == '3':
            sauv = input('Quel personnage sauvegarder ? : ')
            for i in range(len(joueur)):
                if joueur[i].nom == sauv:
                    savePerso(joueur[i])
        elif choix == '4':
            print('Bye !')
            continuer = False

def speelFromClasse(classe): #Attribut les sorts par rapport à la classe choisie
    return {
        'Mage': [Boule_de_feu.nom, Glace.nom],
        'Paladin': [],
        'Guerrier':[],
        'Pretre':[]
    }.get(classe, [])
        
    
if __name__ == '__main__':
    menuPrincipale()
