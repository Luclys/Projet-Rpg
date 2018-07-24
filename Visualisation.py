#-*- coding: utf-8 -*-
import os.path
from random import *
import pickle

from FonctionsPourClasses import *
from Classes import *
from Visualisation import * 


def showPerso(perso): #Montre juste les stats, pas le contenu de l'inventaire ni le stuff
    print("Nom = ",perso.nom)
    print("Pv = ",perso.pv )
    print("Armure = ",perso.armure )
    print("Force = ",perso.force )
    print("Vitesse = ",perso.vitesse )
    print("Critique = ",perso.critique,"%")
    print("Precision = ",perso.precision,"%")
    print("Defense = ",perso.defense )
    print("Prospection = ",perso.prospection )
    print("Classe = ",perso.classe )


def showItem(item):
    print("Nom = ",perso.nom)
    print("Cout = ",perso.cout)
    print("Rarete = ",perso.rarete )
    print("Description = ",perso.description )
    print("Poids = ",perso.poids )
