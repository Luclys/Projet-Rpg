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
    tour_effet = 0
    #Tour pour combat
    tour = 0
    #Emplacements des equipements
    tete = ""
    dos = ""
    bras1 = ""
    bras2 = ""
    pieds = ""
    main = ""
    #Emplacement de transition pour savoir ou doit aller chaque equipement
    tag = ""
    ############
    argent = 0
    exp = 0
    expmax = randint(150, 200) #Choisie aleatoirement l'exp pour atteindre le niveau 2 pour le fun x) 
    niveau = 1
    def __init__(self, nom, pv, pvmax, force, puissance, defense, classe, prospection, critique, precision, vitesse, mana, poidsMax, sort_utilisable, inventaire): 
        self.pv = pv
        self.pvmax = pvmax
        self.force = force
        self.puissance = puissance #Les mages utilisent de la magie donc pas de force mais une stat de puissance pour eux
        self.vitesse = vitesse
        self.critique = critique
        self.precision = precision
        self.defense = defense
        self.mana = mana
        self.prospection = prospection
        self.classe = classe
        self.nom = nom
        self.poidsMax = poidsMax
        self.sort_utilisable = sort_utilisable #Voir les sorts dispo nécéssaires pour les trier etc (dans une liste)
        self.inventaire = inventaire

class Classe:
    def __init__(self, nom, tout_sort):
        self.nom = nom
        self.tout_sort = tout_sort #Tout les sorts de la classe en question (dans une liste)

class PNJ:
    def __init__(self, nom, objet):
        self.nom = nom
        self.objet = objet #Objet qu'il vend (dans une liste)
     
class Monstre:
    def __init__(self, nom, vitesse, pv, pvmax, force, loot, effet, niveau):
        self.nom = nom
        self.vitesse = vitesse
        self.pv = pv
        self.pvmax= pvmax
        self.force = force
        self.loot = loot #une liste qui contient LES NOMS des objets lootables par le monstre
        self.effet = effet
        self.niveau = niveau #Le niveau des mobs pourquoi pas faire un randomizateur et si tu tombes contre un mob lvl 3 il a + de degat que un lvl 2 (et donne + d'exp)
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
        self.degat = degat #si le sort fait des degats
        self.soin = soin #si le sort heal
        self.effet = effet
        self.niveau_requis = niveau_requis #niveau requis pour apprendre le sort
        
class Effet:
    def __init__(self, nom, valeur, tour, description): #la valeur c'est ce que ça fait: ce que ça modifie comme stat,  ou les dégats que ça inflige
        self.nom = nom
        self.valeur = valeur
        self.tour = tour #cb de tour il dure
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
        self.emplacement = emplacement #indique l'emplacement de l'item (c'est un str)
      	
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
        self.emplacement = emplacement #indique l'emplacement de l'item (c'est un str)


class Zone(): #Systeme de zone avec des monstres specifiques a chaque zone 
    def __init__(self, nom, monstre, description):
        self.nom = nom
        self.monstre = monstre #les monstres de la zone (en liste)
        self.description = description
        
