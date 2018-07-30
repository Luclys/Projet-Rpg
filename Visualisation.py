#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *


def showPerso(perso): #Montre juste les stats, pas le contenu de l'inventaire ni le stuff
    print("Nom = ",perso.nom)
    print("Expérience = ",perso.exp)
    print("Niveau = ",perso.niveau)
    print("Pv = ",perso.pv)
    print("Pv max = ",perso.pvmax)
    print("Mana = ", perso.mana)
    print("Armure = ",perso.armure)
    print("Force = ",perso.force)
    print("Vitesse = ",perso.vitesse)
    print("Critique = ",perso.critique,"%")
    print("Precision = ",perso.precision,"%")
    print("Defense = ",perso.defense)
    print("Prospection = ",perso.prospection)
    print("Classe = ",perso.classe)
    print("Argent = ",perso.argent)
    print("Poids Maximum = ",perso.poidsMax)

def showItem(item):
    print("Nom = ",item.nom)
    print("Cout = ",item.cout)
    rareteToStr(item)
    print("Description = ",item.description)
    print("Poids = ",item.poids)
