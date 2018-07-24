#-*- coding: utf-8 -*-
import pickle

from FonctionsPourClasses import *




class Personnage:
    inventaire = dict()
    equippement = list()
    def __init__(self, vitesse, pv, force, defense, classe, prospection, critique, precision, armure, nom, mana, argent):
        
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

    def show(self): #Montre juste les stats, pas le contenu de l'inventaire ni le stuff
        print("Nom = ",self.nom)
        print("Pv = ",self.pv )
        print("Armure = ",self.armure )
        print("Force = ",self.force )
        print("Vitesse = ",self.vitesse )
        print("Critique = ",self.critique,"%")
        print("Precision = ",self.precision,"%")
        print("Defense = ",self.defense )
        print("Prospection = ",self.prospection )
        print("Classe = ",self.classe )
        

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
