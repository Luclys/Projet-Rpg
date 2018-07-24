#-*- coding: utf-8 -*-
import pickle

from FonctionsPourClasses import *




class Personnage:
    inventaire = list()
    equippement = list()
    def __init__(self, vitesse, pv, force, defense, classe, prospection, critique, precision, armure, nom):
        
        self.pv = pv
        self.armure  = armure
        
        self.force = force
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        
        self.defense = defense

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

    
