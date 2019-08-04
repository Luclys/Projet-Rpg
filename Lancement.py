#Ici on met les persos + les items pour test les fonctions et les classes
from Visualisation import *

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


def menuPrincipale():
    continuer = True
    while continuer:
        print("1.Nouveau personnage \n2.Retour à l'aventure !\n3.Virer en donjon !\n4.Sauvegarder\n5.Quitter")
        choix = input('Que voulez-vous faire ? : ')
        if choix == '1':
            nom = input('Entre ton nom : ')
            nom_joueur = list()
            if len(joueur) != 0:
                for j in joueur:
                    nom_joueur.append(j.nom)
            while nom in nom_joueur:
                nom = input('\n***' + nom + ' est déjà utilisé. Entrez un autre nom***\n')
            classe = input('Entre ta classe : ')
            while classe not in classeDispo: #Si l'individu choisi une classe qui n'existe pas (petit coquin)
                classe = input("Cette classe n'existe pas \nSelectionne une des classes si dessous : \n- " + '\n- '.join(classeDispo) + '\n Fais ton choix : ')
            #CREATION DU JOUEUR ON LE STOCK DANS LA LISTE 'joueur' car sinon il ne peut pas etre réutilisé    
            joueur.append(creerPerso(nom, randint(1,5), randint(1,5)\
                                     , randint(1,5), randint(1,5), randint(1,5), classe\
                                     , randint(1,5),randint(1,5),randint(1,5),randint(1,5)\
                                     ,randint(1,5),randint(1,5), eval(classe).get_sort(), dict()))

            joueur[0].get_caracteristique()
        elif choix == '2':
            loadAll()
            
        elif choix == '3':
            loadAll()
        elif choix == '4':
            sauv = input('Quel personnage sauvegarder ? : ')
            for i in range(len(joueur)):
                if joueur[i].nom == sauv:
                    savePerso(joueur[i])
        elif choix == '5':
            print('Bye !')
            continuer = False
        
    
if __name__ == '__main__':
    menuPrincipale()
