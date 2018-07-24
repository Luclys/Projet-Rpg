#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 20:25:40 2017

@author: Zorino, Flywalker, mornviir
"""
#Importation de gros modules colombiens
from Classes_Monstre_Perso_Item_Armes import *
from Fonction_de_sauvegarde import *
from Fonction_de_chargement import *
from Fonction_du_menu import *
from Fonction_concernant_le_mode_AVENTURE import * 
import os.path
from random import *


class Perso:
    
    # Partie des méthodes de création : création du perso, stat, classe, etc...
    
    def __init__(self,nom_perso):
        self.nom_perso = nom_perso
        self.argent = 1000
        self.exp = 0
        self.niveau = 1
        self.inventaire = dict()
        self.equipement = dict()
        self.mains_libres = 2
        
    def def_classe(self,nom_classe):
        self.nom_classe = nom_classe
        
    def def_stats(self,vie,force,armure,agilite,mana):
        perso_stats = {"Vie": vie , "Force": force , "Valeur_Armure": armure , "Agilité": agilite , "Mana": mana}
        self.perso_stats = perso_stats
        
    # Partie des méthode d'affichage : montrer l'inventaire, l'équippement ou le personnage en général        
    
    def show(self):        
        print("Nom : {}\nArgent : {}\nXP: {}\nNiveau : {}\nClasse : {}\nStats : {}".format(self.nom_perso,  self.argent,  self.exp,  self.niveau,  self.nom_classe,  self.perso_stats))                                                                   
    
    def show_inventory(self):
        numero_item_dans_inventaire = 0
        for i in self.inventaire:
            print(numero_item_dans_inventaire,")",i.nom, " : ", self.inventaire[i])
            numero_item_dans_inventaire += 1
            
    def show_equipement(self):   #Impossible de faire de boucle dans un dicos lol 
        numero_arme_dans_inventaire = 0
        for i in self.equipement:
            print(numero_arme_dans_inventaire,")",i.nom, " : ", self.equipement[i])
            numero_arme_dans_inventaire += 1
            
    # Partie des méthode utilitaires : gestion d'objets et d'équippement        
    
    def jeter_Item(self,item):
        self.inventaire[item] -= 1
        if self.inventaire[item] == 0:
            self.inventaire.pop(item)
            
    def desequip(self,arme):                #Ici on met bien l'item dans l'inventaire mais on oublie de vérifier si on l'a en main ou pas xD, ducoup si on l'a pas en main et qu'on déséquipe un item ça duplique l'item :(
        if arme not in self.inventaire:
            self.inventaire[arme] = 1    
        else:
            self.inventaire[arme] += 1
        self.equipement.remove(arme)
        self.mains_libres -= arme.stats["Mains"]
        
    def equip(self,arme):
        if self.mains_libres - arme.stats["Mains"] < 0:
            print("Vous avez les mains pleines")
        else:
            self.equipement[arme] = 1
            self.mains_libres -= arme.stats["Mains"]
    
    def addItemToInventory(self,item,quantité): #Je comprend pas ce que item.nom réprésente vu que c'est pas un objet x)
        if item.nom in self.inventaire : 
            self.inventaire[item] += quantité
        else:
            self.inventaire[item] = quantité

    

############################################## Consommables

class Consommable(Perso):
	
    def __init__(self,nom,cout,description,applications): #application correspond à un dictionnaire qui utilise toutes les valeurs qui seront affectées genre il dit {vie:-20,agi : +32 }...				#le cout c'est pour si on veut faire un système d'argent genre tu revend des items et en rachète (sans marcher)
        self.nom = nom
        self.cout = cout
        self.description = description
        self.applications = applications
        
    def utiliser(self,perso):
        for i in self.applications:
            perso.perso_stats[i] += self.applications[i]
    
    def show(self):
        print("Nom: {}\nCout : {}\nDescription : {}\nApplications : {}".format(self.nom, self.cout, self.description, self.applications))
   
    def spécialshow(self): #sert pour les sauvegardes : les £ sont la pour le double parsage
            return("{}£{}£{}£{}".format(self.nom, self.cout, self.description, self.applications))

############################################## Armes
            
class Armes(Consommable):
    
    def __init__(self,nom,cout,description,stats):
        self.nom = nom
        self.cout = cout
        self.description = description
        self.stats = stats  #écrit sous forme de : DEGATS USURE MAIN -----------> DUM
    def show(self):
        print("Nom: {}\nCout : {}\nDescription : {}\nStats : {}".format(self.nom, self.cout, self.description, self.stats))    
   
############################################## Monstres
class Monstre():
    def Rarete_loot():
        nombre_aleatoire = randint(0,100)
        if nombre_aleatoire in range(0,50):
            return "Commun"
        if nombre_aleatoire in range(50,75):
            return "Rare"
        if nombre_aleatoire in range(75,90):
            return "Super Rare"
        if nombre_aleatoire in range(90,101):
            return "Légendaire !!!"
    
    def __init__(self,nom,niveau,xp):
        self.nom = nom
        self.niveau = niveau
        self.xp = xp
        self.rareté = Rarete_loot()
        
        
    def def_stats(self,vie,force,agilite):
        monstre_stats = {"Vie": vie ,"Force": force ,"Agilité": agilite}
        self.monstre_stats = monstre_stats

#La partie ou on définit de la merde et des fonctions de test : 
    
d = Perso("Omaewa")
d.def_classe("Shindeyuku")
d.def_stats(12,12,12,12,1)
{'Vie': 12, 'Force': 12, 'Valeur_Armure': 12, 'Agilité': 12, 'Mana': 1}
d.exp += 67
a = Consommable("Potion soin",30,"Rend +20 pv",{'Vie': 20})
b = Consommable("Potion force",30,"Donne +10 force",{'Force':10})
c = Consommable("Potion de soinrce",60,"Donne +10 en force et +20 pv",{'Vie':20,"Force":10})
hache = Armes("HACHE",14,"None",{"Dégâts":6,"Usure":23,"Mains":1})
vieil_lance = Armes("Vieil lance",50,"None",{"Dégâts":17,"Usure":12,"Mains":2})
d.addItemToInventory(a,4)
d.addItemToInventory(b,2)
d.addItemToInventory(c,1)
