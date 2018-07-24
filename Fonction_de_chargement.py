#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 10:48:43 2017

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

#fonction perdue, sais pas où la ranger
def déparsagePropre(str):
    str2 = ""
    for i in range(len(str)-1):
        str2 += str[i]
    return str2


#LE CHARGEMENT DU PERSO
###############################"On lance TOUT le module à partir de loadUser, faut juste taper loadUser(perso)
def loadUser(perso):        #parse 1 = ;
    name = input("insérez le nom du personnage (le fichier) : ")
    choix = input("Voulez vous spécifier la destination [O/n]?: ")
    if choix == 'O':
        desti = input('insérez votre destination : ')
    else:
        desti = "/home/mornviir/Documents/python/Projo RPG/users/" + name + "/"    
    usr = open(desti + "usr"+ name, 'r')
    testo = usr.read()
    testo = déparsagePropre(testo)
    L = testo.split(";")  
    perso = Perso(L[0])
    perso.argent = int(L[1])
    perso.exp = int(L[2])
    perso.mains_libres = int(L[3])
    perso.nom_classe = L[4]
    usr.close()
    return loadStats(perso,name,desti)


#LE CHARGEMENT DES STATS
def def_stats(perso,vie,force,armure,agilite,mana):       
    Dstats = {"Vie": vie , "Force": force , "Valeur_Armure": armure , "Agilité": agilite , "Mana": mana}
    perso.Dstats = Dstats   
    
def loadStats(perso,name,desti):       #parse 1 = ;    
    stat = open(desti + "stat"+ name, 'r')
    testo = stat.read()
    testo = déparsagePropre(testo)
    L = testo.split(";")
    L[4] = L[4].replace("\n","")
    def_stats(perso,int(L[0]),int(L[1]),int(L[2]),int(L[3]),int(L[4]))
    stat.close()
    return loadInvent(perso,name,desti)


#LE CHARGEMENT DE L'INVENTAIRE
def loadInvent(perso,name,desti):      #parse 1 = ; ||parse 2 = £    
    invent = open(desti + "invent"+ name, 'r')
    nbr = open(desti + "nbr" + name, 'r')
    NBRtesto = nbr.read()
    NBRtesto = déparsagePropre(NBRtesto)
    NBRL = NBRtesto.split(";")
    #le truc plus sera utilisé pour les tours de boucle lors du ADD ITEM DE L'INFINI
    pvirguletesto = invent.read()
    pvirguletesto = déparsagePropre(pvirguletesto)
    L = pvirguletesto.split(";")
    refnbr = 0
    for i in L:
        L2 = i.split("£") 
        temp = create_item(L2[0],L2[1],L2[2],L2[3])
        perso.addItemToInventory(temp, int(NBRL[refnbr]))
        refnbr += 1
    return perso.show_inventory()
    nbr.close()
    invent.close()         
# str : nom, int : cout, str :  description, dico :  application    
