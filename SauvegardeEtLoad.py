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
        i = int(i)
        i+=1
        i = str(i)
    pickle.dump(perso, open('perso/'+i, 'wb'))

def loadPerso(nom):
    return pickle.load(open('perso/'+nom, 'rb'))

#Cette fonction est juste un test, mais comme elle marche on la garde.
def loadAll(): #    Fonction pour charger tout les personnages et les memoriser dans une liste. (typiquement le truc a lancer au demarrage du jeu)
    i = '0'
    if not os.path.isdir("perso/"):
        print('Aucun personnage enregistré !')
        return 'Aucun personnage enregistré !'
    while os.path.exists('perso/'+i):
        joueur.append(loadPerso(str(i)))
        i = int(i)
        i += 1
        i = str(i)
#PAS ENCORE TESTEE, Faut faire idem pour la sauvegarde (enregistrer les infos dans un dossier au nom du perso pour que ce soit compatible avec le chargement)
def ChargerPerso(perso): #fonction plus complète pour charger à partir d'un Rep
    choix = input("Voulez vous spécifier la destination [O/n]?: ")
    if choix == 'O':
        desti = input('insérez votre destination : ')#il faut mettre la destination à partir de la racine
    name = input("Quel est votre nom jeune aventurier ?: ")
    if os.path.exists(desti + name):
        print("Oh je vous reconnait !!!")
    else: 
        os.makedirs(desti + name,511)
        usr = loadPerso(name)
    return usr
