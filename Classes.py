#-*- coding: utf-8 -*-
import pickle
from SauvegardeEtLoad import *
from Classes import *
from Visualisation import * 
from FonctionImportante import *


##################################  GROUPE PERSONNAGES/MONSTRES/BOSS
class Personnage:
    #Effet appliqué directement
    effet = ""
    tour = 0
    #Emplacements
    tete = ""
    dos = ""
    bras1 = ""
    bras2 = ""
    pieds = ""
    main = ""
    #Emplacement de transition pour savoir ou doit aller l'item
    tag = ""
    ############
    argent = 0
    exp = 0
    expmax = randint(150, 200)
    niveau = 1
    def __init__(self, nom, pv, pvmax, force, puissance, defense, classe, prospection, critique, precision, vitesse, mana, poidsMax, sort_utilisable, inventaire): 
        self.pv = pv
        self.pvmax = pvmax
        self.force = force
        self.puissance = puissance
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        self.defense = defense
        self.mana = mana
        self.prospection = prospection
        self.classe = classe
        self.nom = nom
        self.poidsMax = poidsMax
        self.sort_utilisable = sort_utilisable
        self.inventaire = inventaire

class Classe:
    def __init__(self, nom, tout_sort):
        self.nom = nom
        self.tout_sort = tout_sort
     
class Monstre:
    def __init__(self, nom, vitesse, pv, force, loot, effet):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.force = force
        self.loot = loot #une liste qui contient LES NOMS des objets lootables par le monstre
        self.effet = effet
class Boss(Monstre):
    def __init__(self,defense,armure,sorts,mana):
        self.defense = defense #les boss, contrairement aux sous monstres, ont une stat de défense, et peuvent donc être plus ou moins tanky
        self.armure = armure #Les boss peuvent eux aussi avoir de l'armure
        self.sorts = sorts #liste qui contient tous les sorts que possède le monstre
        self.mana = mana #Pour lancer ses sorts il lui faut du mana
    #Note : les monstres élites sont des miniboss, ils auront donc des stats réduites : peu/pas de sorts ou de faibles stats à côté

############################    GROUPE EFFET/SORT
class Sort:
    def __init__(self, nom, coutMana, description, degat, soin, effet, niveau_requis):
        self.nom = nom
        self.coutMana = coutMana
        self.description = description
        self.degat = degat
        self.soin = soin
        self.effet = effet
        self.niveau_requis = niveau_requis
        
class Effet:
    def __init__(self, nom, valeur, tour, description): #la valeur c'est ce que ça fait: ce que ça modifie comme stat,  ou les dégats que ça inflige
        self.nom = nom
        self.valeur = valeur
        self.tour = tour
        self.description = description


###########################     GROUPE ITEM/CONSO/STUFF/ARME
class Item:
    def __init__(self, nom, cout, rarete, poids, description):
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.description = description
        
class Consommable():
    def __init__(self,nom, cout, rarete, poids, description, effet, valeur): 
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.description = description
        self.effet = effet
        self.valeur = valeur
        
class Equipement():
    def __init__(self, nom, cout, rarete, poids, force, puissance, vitesse, mana, defense, description, effet_sur_joueur, effet_sur_mob, emplacement):
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.force = force
        self.puissance = puissance
        self.vitesse = vitesse
        self.mana = mana
        self.defense = defense
        self.description = description
        self.effet_sur_joueur = effet_sur_joueur
        self.effet_sur_mob = effet_sur_mob
        self.emplacement = emplacement
      	
class Arme():
    def __init__(self, nom, cout, rarete, poids, description, force, puissance, vitesse, mana, defense, effet_sur_joueur, effet_sur_mob, emplacement):
        self.nom = nom
        self.cout = cout 
        self.rarete = rarete
        self.poids = poids
        self.description = description
        self.puissance = puissance
        self.vitesse = vitesse
        self.force = force
        self.mana = mana
        self.defense = defense
        self.effet_sur_joueur = effet_sur_joueur
        self.effet_sur_mob = effet_sur_mob
        self.emplacement = emplacement
