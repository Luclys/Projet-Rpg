#-*- coding: utf-8 -*-
import pickle

from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *

##################################  GROUPE PERSONNAGES/MONSTRES/BOSS
class Personnage:
    inventaire = dict()
    equipement = list()
    emplacements = {"Mains" : 2, "Tete" : 1, "Torse" : 1, "Jambes" : 1, "Pieds" : 1, "Anneaux" : 2}
    argent = 0
    xp = 0
    niveau = 1
    def __init__(self, nom, pv, force, defense, classe, prospection, critique, precision, armure, vitesse, mana, poidsMax): 
        self.pv = pv
        self.armure  = armure
        self.force = force
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        self.defense = defense
        self.mana = mana
        self.prospection = prospection
        self.classe = classe
        self.nom = nom
        self.poidsMax = poidsMax
        
class Monstre:
    def __init__(self, nom, vitesse, pv, force, loot):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.force = force
        self.loot = loot #une liste qui contient LES NOMS des objets lootables par le monstre
        
class Boss(Monstre):
    def __init__(self,defense,armure,sorts,mana):
        self.defense = defense #les boss, contrairement aux sous monstres, ont une stat de défense, et peuvent donc être plus ou moins tanky
        self.armure = armure #Les boss peuvent eux aussi avoir de l'armure
        self.sorts = sorts #liste qui contient tous les sorts que possède le monstre
        self.mana = mana #Pour lancer ses sorts il lui faut du mana
    #Note : les monstres élites sont des miniboss, ils auront donc des stats réduites : peu/pas de sorts ou de faibles stats à côté

############################    GROUPE EFFET/SORT
class Sorts:
    def __init__(self, nom, coutMana, description, valeur):
        self.nom = nom
        self.valeur = valeur
        self.coutMana = coutMana
        self.description = description        

        
class Effet:
    def __init__(self, nom, valeur, duree, description): #la valeur c'est ce que ça fait: ce que ça modifie comme stat,  ou les dégats que ça inflige
        self.nom = nom
        self.valeur = valeur
        self.duree = duree
        self.description = description


###########################     GROUPE ITEM/CONSO/STUFF/ARME
class Item:
    def __init__(self, nom, cout, rarete, poids, description):
        self.nom = nom
        self.cout = cout #un item coute la statistique cout à l'achat. Et rapporte la stat cout/2 à la revente
        self.rarete = rarete
        self.poids = poids
        self.description = description
        
class Consommable(Item): 
    def __init__(self,effet): 
        self.effet = effet
        
class Equipement(Item):
    def __init__(self, durabilite, armure, effet_sur_joueur, effet_sur_mob, emplacement):
      	self.durabilite = durabilite
      	self.armure = armure
      	self.effet_sur_joueur = effet_sur_joueur
      	self.effet_sur_mob = effet_sur_mob
      	self.emplacement = emplacement
      	
class Arme(Equipement):
    def __init__(self, degat):
      	self.degat = degat    
