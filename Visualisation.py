#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from SauvegardeEtLoad import *
from Classes import *

from FonctionImportante import *


def showPerso(perso): #Montre juste les stats, pas le contenu de l'inventaire ni le stuff
    print("Nom = ",perso.nom)
    print("Expérience = ",perso.exp)
    print("Niveau = ",perso.niveau)
    print("Pv = ",perso.pv)
    print("Sorts = ", perso.sort_utilisable)
    print("Pv max = ",perso.pvmax)
    print("Mana = ", perso.mana)
    print("Force = ",perso.force)
    print("Puissance = ",perso.puissance)
    print("Vitesse = ",perso.vitesse)
    print("Critique = ",perso.critique,"%")
    print("Precision = ",perso.precision,"%")
    print("Defense = ",perso.defense)
    print("Prospection = ",perso.prospection)
    print("Classe = ",perso.classe)
    print("Argent = ",perso.argent)
    print("Poids Maximum = ",perso.poidsMax)
    print("Il vous faut ", perso.expmax - perso.exp, " pour atteindre le prochain niveau !") 


def showItem(item):
    print("Nom = ",item.nom)
    print("Cout = ",item.cout)
    rareteToStr(item)
    print("L'item donne ", item.force, " de force")
    print("L'item donne ", item.puissance, " de puissance")
    print("L'item donne ", item.vitesse, " d'accéleration")
    print("L'item donne ", item.mana, " de mana")
    print("L'item donne ", item.defense, " d'armure !")
    print("Description = ",item.description)
    print("Poids = ",item.poids)

def showMarket(PNJ):
    print(PNJ.objet)

