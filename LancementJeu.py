#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *

#Ici on met les persos + les items pour test les fonctions et les classes
Arthur = Personnage("Yolo",5,5,5,5,5,5,5,5,5,5,5)
Poudre_magique = Item("Poudre de perlinpainpain",50,20, 10, "C'est une poudre magiiiiique !")
Ronce_démoniaque = Item("Ronce démoniaque",50,90, 10, "Elle pousse dans le cote cache de la lune.")
gluant = Monstre("Gluant", 5, 5, 5, [Poudre_magique, Ronce_démoniaque])
