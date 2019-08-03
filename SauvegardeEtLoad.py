#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 


joueur = list()


#Fonction des Personnages :

def creerPerso(nom, pv, pvmax, force, puissance, defense, classe, prospection, critique, precision, vitesse, mana, poidsMax, sort_utilisable, inventaire):
    perso  = Personnage(nom, pv, pvmax, force, puissance, defense, classe, prospection, critique, precision, vitesse, mana, poidsMax, sort_utilisable, inventaire)
    return perso
            
def savePerso(perso):         #Permet d'enregistrer un personnage dans un fichier binaire (facile Ã  exploiter par la suite)
    i = '0'
    if not os.path.isdir("perso/"):
        os.mkdir('perso')
    while os.path.exists('perso/'+i):
        perso_open = pickle.load(open('perso/'+i, 'rb'))
        if perso_open.nom == perso.nom:
            choice = input('\n***Personnage déjà sauvegardé.\n***Voulez vous écraser la sauvegarde ? :\n-Oui\n-Non\n ')
            if choice == 'Oui':
                os.remove('perso/'+i)
                pickle.dump(perso, open('perso/'+i, 'wb'))
                print('\n***' + joueur[int(i)].nom + ' a été sauvegardé !***\n')
                return 0
            else:
                return 0
        i = int(i)
        i+=1
        i = str(i)
    pickle.dump(perso, open('perso/'+i, 'wb'))
    print('\n***' + joueur[int(i)].nom + ' a été sauvegardé !***\n')

def loadPerso(nom):
    return pickle.load(open('perso/'+nom, 'rb'))

#Cette fonction est juste un test, mais comme elle marche on la garde.
def loadAll(): #    Fonction pour charger tout les personnages et les memoriser dans une liste. (typiquement le truc a lancer au demarrage du jeu)
    i = '0'
    if not os.path.isdir("perso/"):
        print('Aucun personnage enregistré !')
        return 'Aucun personnage enregistré !'
    nom_joueur = list()
    if len(joueur) != 0:
        for j in joueur:
            nom_joueur.append(j.nom)
    while os.path.exists('perso/'+i):
        if loadPerso(str(i)).nom in nom_joueur:
            input('\n***' + loadPerso(str(i)).nom + ' déjà chargé***\nVoulez vous écraser le personnage en cours ? : \n-Oui\n-Non\n')
            if choice == 'Oui':
                index = nom_joueur.index(loadPerso(str(i)).nom)
                joueur[index] = loadPerso(str(i))
                print('***' + loadPerso(str(i)).nom + ' chargé.\nBon jeu !***')
        else:
            joueur.append(loadPerso(str(i)))
        i = int(i)
        i += 1
        i = str(i)

