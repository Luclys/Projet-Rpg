#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *


class Personnage:
    inventaire = dict()
    equipement = list()
    def __init__(self, nom, pv, force, defense, classe, prospection, critique, precision, armure, vitesse, mana, argent): 
        self.pv = pv
        self.armure  = armure
        self.force = force
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        self.defense = defense
        self.argent = argent
        self.mana = mana
        self.prospection = prospection
        self.classe = classe
        self.nom = nom
        
class Monstre:
    def __init__(self,nom,vitesse,pv,force,loot):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.force = force
        self.loot = loot 

class Effet:
    def __init__(self,nom,valeur,duree,description):
        self.nom = nom
        self.valeur = valeur
        self.duree = duree
        self.description = description

class Item:
    def __init__(self,nom,cout,rarete,poids,description):
        self.nom = nom
        self.cout = cout
        self.rarete = rarete
        self.poids = poids
        self.description = description
        
class Consommable(Item): 
    def __init__(self,effet): 
        self.effet = effet
        
class Equipement(Item):
    def __init__(self,durabilite,armure,effet_sur_joueur,effet_sur_mob,emplacement):
      	self.durabilite = durabilite
      	self.armure = armure
      	self.effet_sur_joueur = effet_sur_joueur
      	self.effet_sur_mob = effet_sur_mob
      	self.emplacement = emplacement
      	
class Arme(Equipement):
    def __init__(self,degat):
      	self.degat = degat    
