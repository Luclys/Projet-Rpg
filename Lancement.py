#Ici on met les persos + les items pour test les fonctions et les classes
from SauvegardeEtLoad import *
import time
import platform
import os

Poudre_magique = Item("Poudre de perlinpainpain",50,3, 10, "C'est une poudre magiiiiique !")
Ronce_demoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
Epee_maudite = Equipement("Epee maudite", 1,90,1, 5, 0, 2, 0, 0,"Ceci est l'épée maudite !","","","main")
Casque_WazukiIV = Equipement("Casque du roi Wazuki IV", 1,1,1, 0, 10, 0, 200, 2,"Vieux casque dégueulasse","","","tete")
Potion_soin = Consommable("Potion de soin",1,1,1,"Potion qui soigne 2 pv", 2, 12)
Brulure = Effet("Brûlure",1,3, "Au secours ça brûle ! Houlàlà")
Stupeur = Effet("Stupeur",1,1, "Oh, bah mince alors, je ne peux plus bouger !"  )
Poison = Effet("Poison",1,3, "J'ai mal, outch")
Hemorragie= Effet("Hémorragie",1,2, "AH PAR L'ATTAQUE DE LA CORNE DE LICORNE, JE SAIGNEEEUUUUH")
Purge = Effet("Purge",0,1, "Je suis guérie. ! Ca va mieux !")
Change_attaque = Effet("Change attaque",10,1, "DE LA PUISSSSSAAAAANNNNNNCCCEEEEEE")
Change_defense = Effet("Change défense",10,1, "Solide comme un rock")
Void = Effet("",0,100000,"")
Gluant = Monstre("Gluant", 5, 13, 20, 1, [Poudre_magique, Ronce_demoniaque], Brulure, 1)
Multi_Gluant = Monstre("Multi Gluant", 5, 13, 20, 1, [Epee_maudite], Poison, 2)
Boule_de_feu = Sort("Boule de feu", 50, "C'est une boule de feu", 10, 0, Brulure, 1)
Glace = Sort("Glace", 50, "Non ce n'est pas celle que tu manges l'été", 10, 0, Purge, 2)
Burst = Sort("Burst", 50, "ça fait mal", 100, -50, Brulure, 5)
Explosion = Sort("explo", 0, "C'est une explosion chirurgicale", 1000, -99999, Void, 0 )
Tension = Sort('Tension', 50, "Augmente la puissance", 0, 0, Change_attaque, 2)
Parade = Sort('Parade', 50, 'Augmente la défense', 0, 0, Change_defense, 2)
DoubleHeal = Sort('Double Heal',75,"Soigne un allié et un adversaire",-50,50, Void, 8)
CoupDboule = Sort("CoupD'Boule",75,"Inflige de lourds dégats grâce à votre front sayant", 999, 1, Void, 72)
DoublePoison = Sort('Double Poison',75,"Empoisonne un allié et un adversaire",0,0, Poison, 8)
DoublePoison = Sort('Double Poison',75,"Empoisonne un allié et un adversaire",0,0, Poison, 8)
Mage = Classe("Mage",[Boule_de_feu.nom, Glace.nom])
Guerrier = Classe("Guerrier",[])
Paladin = Classe("Paladin",[])
Ish = PNJ("Ish", [Epee_maudite.nom, Casque_WazukiIV.nom])

Plaine = Zone("Plaine", [Gluant, Multi_Gluant], "C'est une plaine")

#Classe disponible (ici juste le string. Nécessite une fonction pour attribuer les sorts et les items de base)
classeDispo = ['Mage', 'Paladin', 'Guerrier']
effetDispo =  [Brulure,Poison,Stupeur,Hemorragie,Purge,Change_attaque,Change_defense,Void]
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
            perso[0] = creerPerso(nom, randint(1,5), 10\
                                     , randint(50,51), randint(1,5), randint(1,5), classe\
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
            + "1.Virée en donjon \n2.Sauvegarder !\n3.Ouvrir l'inventaire \n4.Retour au menu principal\n"\
            + '**********************************************************************************************\n')
        choix = input('Que voulez-vous faire ? : ')
        if choix == '1':
            clean()
            donjon(perso)
            
        elif choix == '2':
            savePerso(perso)

        elif choix == '3':
            clean()
            perso.get_inventaire()
            print(perso.empla)
        elif choix == '4':
            clean()
            continuer = False

        else:
            print('\n***Commande inconnue :(***\n\n')


def donjon(perso):
    print('Vous entrez dans le donjon !')
    continuer = True
    while continuer:
        monstre_combat = list()
        nombre_monstre = randint(1,5)
        mob_dispo = gen_mob(nombre_monstre)
        nom_multi_mob(nombre_monstre, mob_dispo, monstre_combat)
        combat(perso,monstre_combat)
        continuer = False

def combat(perso, monstre): #la fonction s'execute par le biais de entre_dans_combat
    monstre_nom = list()
    for i in monstre:
        monstre_nom.append(i.nom)
    print("Tu es contre ", str(monstre_nom))
    pv_total_monstre = 0
    for i in monstre:
        pv_total_monstre += i.pv
    while perso.pv > 0 and pv_total_monstre > 0 :
        perso.tour += 1
        print("Tour : ", perso.tour)
        print("Effet actuel : ", perso.get_effet(), " pendant encore : ", perso.get_tour_effet())
        if perso.get_effet():
            for i in effetDispo:
                if perso.get_effet() == i.nom:
                    print("*** L'effet t'inflige " + str(i.valeur) + ' points de dégat, outch !***')
                    i.applique_dommage_effet(perso)
                    print("PV apres l'effet : " + str(perso.pv))
        choix = input("Que voulez-vous faire ? : \n1.Attaquer\n2.Fuir\n")
        if choix == '1':
            for i in monstre:
                if i.pv > 0:
                    print(i.nom + '\n')
            avancer = False
            while avancer == False:
                choix2 = input("\nQui attaquer ? : ")
                for i in monstre:
                    if i.nom == choix2 and i.pv > 0 :
                        cible = i
                        avancer = True
            cible.pv -= perso.force
            print("Tu attaques " + cible.nom + ' !\nIl perd '\
                  + str(perso.force) + ' !\n' + cible.nom + ' possède ' + str(cible.pv)+ ' PV\n')
            for i in monstre:
                pv_total_monstre += i.pv
        print('Les monstres attaquent !')
        for i in monstre:
            if i.pv > 0:
                print(i.nom + " t'infliges "+ str(i.force) + " !")
                perso.pv -= i.force
                print('Il te reste ' + str(perso.pv))
                cible.effet.applique_effet_de_mob(perso, cible)
    if perso.pv <= 0 :
        print("Tu as été battu !")
        perso.pv = perso.pvmax
        perso.set_effet('')
        perso.tour_effet = 0
    else :
        print("Bravo, votre ennemi est mort !")
        perso.set_effet('')
        perso.lootRarete(choice(monstre))
        perso.donne_exp( choice(monstre))
        perso.donne_argent( choice(monstre))
        perso.tour_effet = 0








def nom_multi_mob(n, mob_dispo, monstre_combat):
    for i in range(n): 
        monstre_tempo = choice(mob_dispo)
        if monstre_tempo not in monstre_combat:
            acc = 0
            nom_base_mob = monstre_tempo.nom
            for i in monstre_combat:
                if monstre_tempo.nom == i.nom:
                    acc += 1
                    monstre_tempo.nom = nom_base_mob + ' ' + str(acc)
            if acc:
                monstre_tempo.nom = nom_base_mob + ' ' + str(acc)
            monstre_combat.append(monstre_tempo)

            
def gen_mob(nb_mob):
    nom_mob = ['Gluant', 'Mega Gluant', 'Sanglier', 'Moskito', 'Bouftou']
    liste_finale = list()
    for i in range(nb_mob):
        nom = choice(nom_mob)
        niveau = randint(1,5)
        pv = randint(10,20)+niveau
        liste_finale.append(Monstre(nom, randint(1,10), pv, pv, 1, [Poudre_magique, Ronce_demoniaque], Brulure, niveau))
    return liste_finale


def clean():   
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    menuPrincipale(perso)
