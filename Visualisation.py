#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle
from SauvegardeEtLoad import *
from Classes import *
from FonctionImportante import *


def showItem(item):
    print("Nom = ",item.nom)
    print("Cout = ",item.cout)
    rareteToStr(item) #Rareté de l'item
    print("L'item donne ", item.force, " de force")
    print("L'item donne ", item.puissance, " de puissance")
    print("L'item donne ", item.vitesse, " d'accéleration")
    print("L'item donne ", item.mana, " de mana")
    print("L'item donne ", item.defense, " d'armure !")
    print("Description = ",item.description)
    print("Poids = ",item.poids)

######## Groupe de système de tour  
def entre_dans_combat(perso, zone): #Doit etre appeller pour faire un combat
    print("Phase 1 tu rentres dans un combat")
    choix = randint(0,(len(zone.monstre) - 1))
    choix_monstre = zone.monstre[choix]
    combat(perso,choix_monstre)

def combat(perso, monstre): #la fonction s'execute par le biais de entre_dans_combat
    print("Tu es contre un ", monstre.nom)
    while perso.pv > 0 and monstre.pv > 0 :
        perso.tour += 1
        print("Tour : ", perso.tour)
        print("Effet actuel : ", perso.effet, " pendant encore : ", perso.tour_effet)
        applique_dommage_effet(perso, monstre.effet)
        choix = input("Que voulez-vous faire ?")
        if choix == "Attaque" or choix == "attaque":
            monstre.pv -= perso.force
            print("Monstre : ", monstre.pv)
        applique_effet_de_mob(perso,monstre.effet, monstre)
        perso.pv -= monstre.force
        print("Moi : ", perso.pv)
    if perso.pv <= 0 :
        print("Perdu!")
        monstre.pv == monstre.pvmax
    else :
        print("Bravo, votre ennemi est mort !")
        lootRarete(monstre, perso)
        donne_exp(perso, monstre)
        donne_argent(perso, monstre)
        monstre.pv = monstre.pvmax
        perso.effet = ""
        perso.tour_effet = 0
